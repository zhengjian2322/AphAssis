import mongoengine
from mongoengine import Document, StringField


class imageModel(mongoengine.Document):
    image_key = mongoengine.StringField(required=True)
    image_value = mongoengine.StringField()