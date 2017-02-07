from peewee import CharField, ForeignKeyField

from model.BaseModel import BaseModel
from model.School import School


class City(BaseModel):
    city_name = CharField()
    nearest_school = ForeignKeyField(School, related_name='city_school_cities')