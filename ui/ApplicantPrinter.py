class ApplicantPrinter():
    @classmethod
    def printList(cls, applicants):
        for applicant in applicants:
            cls.print(applicant)

    @classmethod
    def print(cls, applicant):
        print("Name: {} {}".format(applicant.first_name, applicant.last_name),
              "Code: {}".format(applicant.application_code))