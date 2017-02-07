from model.Applicant import Applicant


class ApplicantQueries():
    @classmethod
    def filter(cls, applicant_city=None, first_name=None, application_code=None, status=None):
        expressions = []
        if(applicant_city != None):
            expressions.append(Applicant.applicant_city == applicant_city)
        if (first_name != None):
            expressions.append(Applicant.first_name == first_name)
        if (application_code != None):
            expressions.append(Applicant.applicant_code == application_code)
        if (status != None):
            expressions.append(Applicant.status == status)

        return Applicant.select().where(expressions)

    @classmethod
    def findStatusByCode(cls, application_code):
        cls_filter = cls.filter(application_code=application_code)

        return cls_filter.get().status

    @classmethod
    def findSchoolByCode(cls, application_code):
        cls_filter = cls.filter(application_code=application_code)

        return cls_filter.get()

    @classmethod
    def findApplicantWithStatusNew(cls):
        return filter(status="New").get()
