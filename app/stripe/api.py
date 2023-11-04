from fastapi import APIRouter, Header

from json import JSONDecodeError

import stripe
from sentry_sdk import capture_exception
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from stripe import Event
from stripe.error import SignatureVerificationError

from app.core.logs import logger
from app.stripe.services import StripeCheckoutService
from settings.base import settings

router = APIRouter(tags=["Payments Endpoints"])


@router.post("/v1/integrations/stripe", include_in_schema=False)
async def stripe_webhook(request: Request, stripe_signature: str = Header(str)):
    try:
        payload = await request.body()
        event: Event = stripe.Webhook.construct_event(payload, stripe_signature, settings.STRIPE_WEBHOOK_SECRET)
        logger.info(f"Received event: {event}")
        if event.type == "checkout.session.completed":
            logger.info(f"Checkout session completed for {event.data.object.id}")
            stripe_service = StripeCheckoutService(event=event)
            await stripe_service.handle_package_checkout()
        return Response(status_code=status.HTTP_200_OK)
    except JSONDecodeError as e:
        logger.error(f"JSONDecodeError: {e}")
        capture_exception(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        logger.error(f"ValueError: {e}")
        capture_exception(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    except SignatureVerificationError as e:
        logger.error(f"SignatureVerificationError: {e}")
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
