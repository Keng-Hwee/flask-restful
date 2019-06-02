from ma import ma
from models.confirmation import ConfirmationModel


class ConfirmationSchema(ma.ModelSchema):
    class Meta:
        model = ConfirmationModel
        load_only = ("user",)  # we do not want to dump the user information
        dump_only = (
            "id",
            "expired_at",
            "confirmed",
        )  # things we are not expecting to pass to the model
        include_fk = True  # so that the foreign key user_id is included in the dump
