import base64

import sendgrid
from sendgrid import Attachment, Disposition, FileContent, FileName, FileType, Mail

from app.core.logs import logger
from settings.base import settings


class EmailService:
    @staticmethod
    def send_email_to_user(user_email: str, message_subject: str):
        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

        logger.info(f"Sending email to: {user_email}")
        from_email = settings.EMAIL_FROM
        subject = message_subject
        html_content = """<p>Witaj!</p>"""

        # html_content = f"{magic_link_url}"
        mail = Mail(from_email=from_email, to_emails=user_email, subject=subject, html_content=html_content)
        try:
            response = sg.send(mail)
            logger.info(response.status_code)
            return True
        except Exception as e:
            logger.info(e)
            return False
