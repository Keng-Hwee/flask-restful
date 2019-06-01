import requests
from flask import request, url_for
from requests import Response, post

from db import db

MAILGUN_DOMAIN ="sandbox2b49ede305fb402a91bf7c5493373045.mailgun.org"
MAILGUN_API_KEY = "0f847539e665e6d92c123e0d8177ecf3-39bc661a-180090ae"
FROM_TITLE = "KH REST API"  # Name of the sender
FROM_EMAIL = "mailgun@sandbox2b49ede305fb402a91bf7c5493373045.mailgun.org"


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    activated = db.Column(
        db.Boolean, default=False
    )  # if we don't set, default is false

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    def send_confirmation_email(
            self
    ) -> Response:  # response is smth which another API gives us
        # talk to Mailgun and return whatever Mailgun responds with
        link = request.url_root[:-1] + url_for(
            "userconfirm", user_id=self.id
        )  # get the route for UserConfirm resource
        # link = http://127.0.0.1:5000/user_confirm/1

        return requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", f"{MAILGUN_API_KEY}"),
            data={
                "from": f"{FROM_TITLE} <{FROM_EMAIL}>",
                "to": [self.email],
                "subject": "Registration confirmation",
                "text": f"Please click the link to confirm your registration: {link}"
            }
        )

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
