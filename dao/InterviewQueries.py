from model import Applicant
from model.Interview import Interview


class InterviewQueries():
    @classmethod
    def findInterviewsByApplicantCode(cls, application_code):
        return Interview.select().join(Applicant).where(Applicant.applicant_code == application_code)