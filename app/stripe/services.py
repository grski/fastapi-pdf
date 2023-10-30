import stripe

from app.core.logs import logger
from app.emails.services import EmailService


class StripeCheckoutService:
    def __init__(self, event):
        self.event = event
        self.stripe_session = stripe.checkout.Session.retrieve(
            self.event["data"]["object"]["id"], expand=["line_items"]
        )
        self.email, self.name, self.line_item = self.extract_data_from_event()

    def __str__(self):
        return f"StripeService for {self.email} - {self.name}, {self.line_item}"

    def extract_data_from_event(self):
        email = self.stripe_session.customer_details["email"]
        line_item = self.stripe_session.line_items["data"][0]["description"]
        name = self.stripe_session.customer_details["name"]
        logger.info(f"Processing stripe session {self.stripe_session}")
        logger.info(f"Processing line item for - {name} - {email}, {line_item}")
        return email, name, line_item

    async def handle_package_checkout(self):
        logger.info(f"Processing package checkout for {self.email} - {self.name}, {self.line_item}")
        logger.info("Adding consultation to user")
        EmailService.send_email_to_user(self.email, "Email from Stripe")

    @property
    def is_checkout_completed(self):
        return self.event["type"] == "checkout.session.completed"
