from peewee import ForeignKeyField

from model.Applicant import Applicant
from model.BaseModel import BaseModel
from model.InterviewSlot import InterviewSlot


class Interview(BaseModel):
    slot_id = ForeignKeyField(InterviewSlot, null=True, related_name='interview_interviewslot_id')
    applicant_code = ForeignKeyField(Applicant, related_name='interview_applicant_code')