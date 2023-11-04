import sendgrid
from sendgrid import Mail
from sentry_sdk import capture_exception

from app.core.logs import logger
from app.emails.constants import EXAMPLE_TEMPLATE
from settings.base import settings


class EmailService:
    @staticmethod
    def send_email_to_user(user_email: str, message_subject: str):
        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

        logger.info(f"Sending email to: {user_email}")
        from_email = settings.EMAIL_FROM
        subject = message_subject
        html_content = EXAMPLE_TEMPLATE
        mail = Mail(from_email=from_email, to_emails=user_email, subject=subject, html_content=html_content)
        try:
            response = sg.send(mail)
            logger.info(response.status_code)
        except Exception as e:
            logger.error(e)
            capture_exception(e)
            return False
        else:
            return True
