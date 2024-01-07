import os
import traceback
import sys
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


class _EmailClient:
    def __init__(self):
        self.smtp_address = os.getenv("SMTP_ADDRESS")

        self.email_from = os.getenv("EMAIL_FROM")
        self.email_to = os.getenv("EMAIL_TO")
        self.email_user = os.getenv("EMAIL_USER")
        self.email_pw = os.getenv("EMAIL_PW")


_client = _EmailClient()


def _get_traceback_msg(exc_type, exc_error, exc_tb):
    lines = traceback.format_exception(exc_type, exc_error, exc_tb)
    full_traceback_text = "".join(lines)

    return full_traceback_text


def send_error():
    exc_error = sys.exc_info()[1]
    exc_type = type(exc_error)
    exc_tb = exc_error.__traceback__  # type: ignore

    traceback_msg = _get_traceback_msg(exc_type, exc_error, exc_tb)
    print(traceback_msg)

    html_content = f"""
            <h4>An unexpected error has occurred!</h4>

            <code>
                {traceback_msg}
            </code>    

            <h6>This is an automated message.</h6>
            """

    msg = EmailMessage()
    msg["Subject"] = f"[ERR] - Twitter @WisdomWordsOnly"
    msg["From"] = _client.email_from  # type: ignore
    msg["To"] = _client.email_to  # type: ignore
    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP(_client.smtp_address) as server:  # type: ignore
        server.starttls()
        server.login(_client.email_user, _client.email_pw)  # type: ignore
        server.send_message(msg)
