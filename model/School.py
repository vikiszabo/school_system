from peewee import CharField

from model.BaseModel import BaseModel


class School(BaseModel):
    city = CharField()