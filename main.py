import os

from generator.MentorInterviewDateGenerator import MentorInterviewDateGenerator
from applicant_interview_details import interview_details
from build import BuildTable
from generator.InterviewGenerator import InterviewGenerator
from dao.ApplicantQueries import ApplicantQueries
from dao.InterviewQueries import InterviewQueries
from generator.ExampleDataGenerator import ExampleDataGenerator
from generator.ApplicantsGenerator import ApplicantsGenerator
from ui.InterviewPrinter import InterviewPrinter


def clear_sreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    chosen_menu = 'q'

    clear_sreen()
    while chosen_menu != 0:
        print("\n- - - School system - Main Menu - - -\n-------------------------------------")
        print("1. I am an administrator")
        print("2. I am a mentor")
        print("3. I am an applicant")
        print("0. Exit")
        print("-------------------------------")
        chosen_menu = int(input("Please choose a menu number: "))

        if chosen_menu == 1:
            clear_sreen()
            chosen_administrator_menu = 'q'
            while chosen_administrator_menu != 0:
                print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
                print("1. Create tables")
                print("2. Generate data")
                print("3. Generate applicants")
                print("4. Generate interview date to applicants")
                print("0. Exit")
                print("-------------------------------------")
                chosen_administrator_menu = int(input("Please choose an Administrator menu number: "))

                if chosen_administrator_menu == 1:
                    try:
                        BuildTable()
                        print("Tables created succcessfully")
                    except:
                        print("I can't create tables")

                elif chosen_administrator_menu == 2:
                    try:
                        ExampleDataGenerator.generate()
                        print("Data successfully generated and inserted")
                    except:
                        print("I can't Generate example data")

                elif chosen_administrator_menu == 3:
                    try:
                        ApplicantsGenerator()
                        print("Applicants data successfully generated and inserted")
                    except:
                        print("I can't Generate applicants")

                elif chosen_administrator_menu == 4:
                    try:
                        InterviewGenerator()
                        print("Interview dates successfully generated to applicants")
                    except:
                        print("Something went wrong. I can't generate interview dates to applicants")

                elif chosen_administrator_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")



        elif chosen_menu == 2:
            clear_sreen()
            chosen_mentor_menu = 'q'
            while chosen_mentor_menu != 0:
                print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
                print("1. Interviews")
                print("0. Exit")
                print("-------------------------------------")
                chosen_mentor_menu = int(input("Please choose a Mentor menu number: "))
                if chosen_mentor_menu == 1:
                    mentor_id = int(input("Please tell me your mentor id: "))
                    try:
                        MentorInterviewDateGenerator(mentor_id)
                    except:
                        print("There is no mentor with that id")

                elif chosen_mentor_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 3:
            clear_sreen()
            chosen_applicant_menu = 'q'
            while chosen_applicant_menu != 0:
                print("\n- - - School system - Applicant Menu - - -\n-------------------------------------")
                print("1. Interview details")
                print("2. Status details")
                print("3. School details")
                print("0. Exit")
                print("-------------------------------------")
                chosen_applicant_menu = int(input("Please choose an Applicant menu number: "))

                if chosen_applicant_menu == 1:
                    application_code = input("Please, enter your application code: ")
                    interviews = InterviewQueries.findInterviewsByApplicantCode(application_code)
                    InterviewPrinter.printList(interviews)
                elif chosen_applicant_menu == 2:
                    application_code = input("Please, enter your application code: ")
                    try:
                        status = ApplicantQueries.findStatusByCode(application_code)
                        print("Your application status is", status)
                    except:
                        print("There is no application code like that in the database. Please try again")

                elif chosen_applicant_menu == 3:
                    application_code = input("Please, enter your application code: ")
                    try:
                        school = ApplicantQueries.findSchoolByCode(application_code)
                        print("Your applied school is", school.city)
                    except:
                        print("There is no application code like that in the database. Please try again")
                elif chosen_applicant_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 0:
            print("\n------------------------------------------------------------")
            print("| Thanks for choosing Codeorgo Software! See you next time!|")
            print("------------------------------------------------------------")
        else:
            print("Wrong menu number was given")


main()
