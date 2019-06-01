from ma import ma
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = (
            "id",
            "activated",
        )  # properties not passed when we create the model
