from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse

import uuid

from starlette import status

from app.core.logs import logger
from app.db import user_queries
from app.emails.services import EmailService
from app.users.constants import COOKIE_EXPIRE_TIME
from app.users.models import UserInvitation
from app.users.services import InvitationKeyService, get_active_user_or_raise
from settings.base import settings

router = APIRouter(tags=["Users Endpoints"])


@router.get("/v1/users", status_code=status.HTTP_200_OK)
async def get_users(request: Request):
    get_active_user_or_raise(request)
    return Response(status_code=status.HTTP_200_OK, content="OK")


@router.post("/v1/user/invitation", status_code=status.HTTP_201_CREATED)
async def send_invitation_key(invitation_key: UserInvitation) -> dict:
    user = user_queries.get_user_by_email(email=invitation_key.user_email)
    if user:
        user_uuid = user["uuid"]
    else:
        user_uuid = str(uuid.uuid4())
        user = user_queries.post_user(
            name=invitation_key.name,
            email=invitation_key.user_email,
            is_confirmed=False,
            uuid=user_uuid,
        )
    logger.info(f"User: {user}")
    invitation_uuid = str(uuid.uuid4())
    invitation_key.uuid = invitation_uuid
    user_queries.post_invitation_key(
        uuid=invitation_uuid,
        user_uuid=user_uuid,
        user_email=invitation_key.user_email,
        is_used=False,
    )
    logger.info(f"Invitation key: {invitation_key}")
    invitation_key_link = InvitationKeyService().generate_invite_key_link(uuid=invitation_uuid)
    EmailService.send_email_to_user(
        invitation_key.user_email,
        invitation_key_link,
        "Invitation to join the app",
    )
    return {"invitation_key": invitation_key}


@router.get("/v1/magic-link/{uuid}", status_code=status.HTTP_200_OK)
async def get_invite_key(uuid: str) -> dict:
    logger.info(f"UUID: {uuid}")
    invitation_key = user_queries.get_invitation_key(uuid=uuid)
    if not invitation_key:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invitation key not found")
    if invitation_key["is_used"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invitation key already used")
    logger.info(f"Invitation key: {invitation_key}")
    user = user_queries.get_user_by_email(email=invitation_key["user_email"])
    confirmed_user = user_queries.update_user_is_confirmed(is_confirmed=True, email=invitation_key["user_email"])
    logger.info(f"Confirmed user: {confirmed_user}")
    logger.info(f"User: {user}")
    user_queries.update_invitation_key_is_used(is_used=True, uuid=uuid)
    logger.info(f"Invitation key: {invitation_key}")
    response = RedirectResponse(url=settings.APP_ENTRYPOINT)
    response.set_cookie(
        key="user_uuid",
        value=invitation_key["user_uuid"],
        expires=COOKIE_EXPIRE_TIME,
        httponly=True,
    )
    return response


@router.post("/v1/login", status_code=status.HTTP_200_OK)
async def login(email: str) -> dict:
    user = user_queries.get_user_login_by_email(email=email)
    logger.info(f"User: {user}")
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not user["is_confirmed"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not confirmed")
    invitation_uuid = str(uuid.uuid4())
    user_queries.post_invitation_key(
        uuid=invitation_uuid,
        user_uuid=user["uuid"],
        user_email=user["email"],
        message_limit=user["messages_left"],
        is_used=False,
    )
    invitation_key_link = InvitationKeyService().generate_invite_key_link(uuid=invitation_uuid)
    EmailService.send_email_to_user(
        user["email"],
        invitation_key_link,
        "Invitation to join the app",
    )
    return {"user": user, "invitation_key_link": invitation_key_link}


@router.get("/v1/send-email", status_code=status.HTTP_200_OK)
async def send_email(email: str):
    EmailService.send_email_to_user(
        email,
        "Test email from FastAPI",
    )
    return Response(status_code=status.HTTP_200_OK, content="Email sent")
