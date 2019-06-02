import os
from typing import List
from requests import Response, post

FAILED_LOAD_API_KEY = "Failed to load Mailgun API key"
FAILED_LOAD_DOMAIN = "Failed to load Mailgun domain."
FAILED_SENDING_EMAIL = "Error in sending confirmation email. User registration failed."


class MailgunException(Exception):
    # message refers to the error message. By creating our own class like this,
    # When an exception is raised, we immed know that it is mailgun's error
    def __init__(self, message: str):
        super().__init__(message)


class Mailgun:
    MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
    FROM_TITLE = "KH REST API"  # Name of the sender
    FROM_EMAIL = "mailgun@sandbox2b49ede305fb402a91bf7c5493373045.mailgun.org"

    @classmethod
    def send_email(
        cls, email: List[str], subject: str, text: str, html: str
    ) -> Response:  # response is smth which another API gives us
        # talk to Mailgun and return whatever Mailgun responds with

        if cls.MAILGUN_API_KEY is None:
            raise MailgunException(FAILED_LOAD_API_KEY)

        if cls.MAILGUN_DOMAIN is None:
            raise MailgunException(FAILED_LOAD_DOMAIN)

        response = post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", f"{cls.MAILGUN_API_KEY}"),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html,
            },
        )

        if response.status_code != 200:
            raise MailgunException(FAILED_SENDING_EMAIL)

        return response
