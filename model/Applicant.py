from peewee import CharField, ForeignKeyField

from model.BaseModel import BaseModel
from model.School import School


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    applicant_city = CharField()
    applicant_code = CharField(null=True)
    applied_school = ForeignKeyField(School, null=True, related_name='applicants')
    status = CharField(null=True)
