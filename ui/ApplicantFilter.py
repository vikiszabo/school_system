from dao import ApplicantQueries
from ui.ApplicantPrinter import ApplicantPrinter


class ApplicantFilter():
    @classmethod
    def location(cls):
        location = input("Please, choose a city!")
        ApplicantPrinter.printList(ApplicantQueries.filter(location=location))
