from peewee import DateTimeField, BooleanField, ForeignKeyField

from model.BaseModel import BaseModel
from model.Mentor import Mentor


class InterviewSlot(BaseModel):
    start_time = DateTimeField()
    end_time = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name='interviewslot_mentor_id')