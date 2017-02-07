class InterviewPrinter():
    @classmethod
    def printList(cls, interviews):
        if len(interviews) == 0:
            print("Wrong code! Please, try again!")
        for i in interviews:
            print(i.applicant_code.first_name, i.applicant_code.last_name, "\n",
                  "Your school is Codecool", i.applicant_code.applied_school.city, "\n",
                  "Your interview date:", i.slot_id.start_time, "\n",
                  "Your mentor is", i.slot_id.mentor.first_name, i.slot_id.mentor.last_name)