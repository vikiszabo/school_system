from peewee import CharField, ForeignKeyField

from model.BaseModel import BaseModel
from model.School import School


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='mentor_school_city')