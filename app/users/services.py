from fastapi import HTTPException

from app.core.logs import logger
from app.db import user_queries
from app.users.constants import FailureConstants
from app.users.models import User
from settings.base import settings


class InvitationKeyService:
    def __init__(self):
        self.url = settings.INVITE_KEY_URL + "v1/magic-link/"

    def generate_invite_key_link(self, uuid: str) -> str:
        return self.url + uuid


def get_active_user_or_raise(request) -> User:
    user_uuid = request.cookies.get("user_uuid")
    logger.info(f"User UUID: {user_uuid}")
    user = user_queries.get_user_uuid(uuid=user_uuid)
    if not user:
        raise HTTPException(status_code=401, detail=FailureConstants.USER_NOT_FOUND)
    if not user["is_confirmed"]:
        raise HTTPException(status_code=403, detail=FailureConstants.USER_NOT_CONFIRMED)
    user_queries.get_invitation_key_user_uuid(user_uuid=user_uuid)
    return User(**user)
