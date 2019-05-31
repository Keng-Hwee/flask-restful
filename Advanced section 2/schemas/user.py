from ma import ma
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = (
            UserModel
        )  # fields for the user schema will follow the user model's sql columns
        load_only = (
            "password",
        )  # password field is only for loading data. Never dumped when we respond to users
        dump_only = ("id",)
