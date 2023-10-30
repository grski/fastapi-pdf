import stripe

from settings.base import settings

stripe.api_key = settings.STRIPE_API_KEY
