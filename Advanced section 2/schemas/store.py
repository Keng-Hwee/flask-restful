from ma import ma
from models.store import StoreModel
from models.item import ItemModel
from schemas.item import ItemSchema


class StoreSchema(ma.ModelSchema):
    items = ma.Nested(
        ItemSchema, many=True
    )  # the store contains many item schema, so the items property is not something we are going to be loading,
    # but smth we gonna be dumping

    class Meta:
        model = StoreModel
        dump_only = ("id",)
        include_fk = True
