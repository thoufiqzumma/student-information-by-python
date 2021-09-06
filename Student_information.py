# STUDENT INFORMATION
import sys

STUDENT_ID = []
STUDENT_NAME = []
STUDENT_AGE = []
STUDENT_SEX = []
STUDENT_FATHER_NAME = []
STUDENT_MOTHER_NAME = []
STUDENT_LAST_EDUCATION = []


class STUDENT_INFORMATION_SYSTEM:
    @staticmethod
    #   THIS FUNCTION HELP TO 'ADD' DATA OF STUDENT.
    def ADD_STUDENT_INFORMATION():
        print("ADDING STUDENT INFORMATION : \n")

        print("ENTER STUDENT ID :", end=" ")
        ID = int(input())
        STUDENT_ID.append(ID)

        print("ENTER STUDENT NAME :", end=" ")
        NAME = input().upper()
        STUDENT_NAME.append(NAME)

        print("ENTER STUDENT AGE :", end=" ")
        AGE = int(input())
        STUDENT_AGE.append(AGE)

        print("ENTER STUDENT SEX :", end=" ")
        SEX = (input())
        STUDENT_SEX.append(SEX)

        print("ENTER STUDENT FATHER_NAME :", end=" ")
        FATHER_NAME = (input())
        STUDENT_FATHER_NAME.append(FATHER_NAME)

        print("ENTER STUDENT MOTHER_NAME :", end=" ")
        MOTHER_NAME = input()
        STUDENT_MOTHER_NAME.append(MOTHER_NAME)

        print("ENTER STUDENT LAST_EDUCATION :", end=" ")
        LAST_EDUCATION = input()
        STUDENT_LAST_EDUCATION.append(LAST_EDUCATION)

    @staticmethod
    #   THIS FUNCTION HELP TO 'DELETE' DATA OF STUDENT
    def DELETE_STUDENT_INFORMATION():
        print("DELETING STUDENT INFORMATION : \n")

        if len(STUDENT_NAME) == 0 and len(STUDENT_ID) == 0 and len(STUDENT_AGE) == 0 and len(
                STUDENT_SEX) == 0 and len(STUDENT_FATHER_NAME) == 0 and len(STUDENT_MOTHER_NAME) == 0 and len(
                STUDENT_LAST_EDUCATION) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            print("ENTER STUDENT'S ID :", end=" ")
            ID = int(input())
            LOC = STUDENT_ID.index(ID)

            STUDENT_ID.remove(STUDENT_ID[LOC])
            STUDENT_NAME.remove(STUDENT_NAME[LOC])
            STUDENT_AGE.remove(STUDENT_AGE[LOC])
            STUDENT_SEX.remove(STUDENT_SEX[LOC])
            STUDENT_FATHER_NAME.remove(STUDENT_FATHER_NAME[LOC])
            STUDENT_MOTHER_NAME.remove(STUDENT_MOTHER_NAME[LOC])
            STUDENT_LAST_EDUCATION.remove(STUDENT_LAST_EDUCATION[LOC])

            print("\n")
            print("\t\t STUDENT INFORMATION DELETED SUCCESSFULLY.")
            print("\n")

    @staticmethod
    #    THIS FUNCTION HELP TO 'UPDATE' DATA OF STUDENT.
    def UPDATE_STUDENT_INFORMATION():
        print("UPDATE STUDENT INFORMATION : \n")

        if len(STUDENT_NAME) == 0 and len(STUDENT_ID) == 0 and len(STUDENT_AGE) == 0 and len(
                STUDENT_SEX) == 0 and len(STUDENT_FATHER_NAME) == 0 and len(STUDENT_MOTHER_NAME) == 0 and len(
                STUDENT_LAST_EDUCATION) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            print("ENTER STUDENT ATTRIBUTE YOU WANT TO DELETE :", end="\n")
            print("LIKE 'ID,NAME,AGE,SEX,FATHER_NAME,MOTHER_NAME,LAST_EDUCATION")
            print("ENTER HERE :", end=" ")
            ATTRIBUTE = input().upper()

            if ATTRIBUTE == 'NAME':
                print("ENTER 'OLD NAME' :", end=" ")
                OLD_NAME = input()
                LOC_NAME = STUDENT_NAME.index(OLD_NAME)

                print("ENTER 'NEW NAME' :", end=" ")
                NEW_NAME = input()
                STUDENT_NAME[LOC_NAME] = NEW_NAME
                print("\t 'NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'NEW ID':
                print("ENTER 'OLD ID' :", end=" ")
                OLD_ID = int(input())
                LOC_ID = STUDENT_ID.index(OLD_ID)

                print("ENTER 'NEW ID NUMBER' :", end=" ")
                NEW_ID = int(input())
                STUDENT_ID[LOC_ID] = NEW_ID
                print("\t 'ID NUMBER UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'AGE':
                print("ENTER 'OLD AGE' :", end=" ")
                OLD_AGE = int(input())
                LOC_ROLL = STUDENT_AGE.index(OLD_AGE)

                print("ENTER 'NEW AGE' :", end=" ")
                NEW_AGE = int(input())
                STUDENT_AGE[LOC_ROLL] = NEW_AGE
                print("\t 'AGE UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'SEX':
                print("ENTER 'OLD SEX' :", end=" ")
                OLD_SEX = (input())
                LOC_SEX = STUDENT_SEX.index(OLD_SEX)

                print("ENTER 'NEW SEX' :", end=" ")
                NEW_SEX = (input())
                STUDENT_SEX[LOC_SEX] = NEW_SEX
                print("\t 'SEX UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'FATHER_NAME':
                print("ENTER 'OLD FATHER_NAME' :", end=" ")
                OLD_FATHER_NAME = input()
                LOC_FATHER_NAME = STUDENT_FATHER_NAME.index(OLD_FATHER_NAME)

                print("ENTER 'NEW FATHER_NAME' :", end=" ")
                NEW_FATHER_NAME = input()
                STUDENT_FATHER_NAME[LOC_FATHER_NAME] = NEW_FATHER_NAME
                print("\t 'FATHER_NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'MOTHER_NAME':
                print("ENTER 'OLD MOTHER_NAME' :", end=" ")
                OLD_MOTHER_NAME = input()
                LOC_MOTHER_NAME = STUDENT_MOTHER_NAME.index(OLD_MOTHER_NAME)

                print("ENTER 'NEW MOTHER_NAME' :", end=" ")
                NEW_MOTHER_NAME = input()
                STUDENT_MOTHER_NAME[LOC_MOTHER_NAME] = NEW_MOTHER_NAME
                print("\t 'MOTHER_NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'LAST_EDUCATION':
                print("ENTER 'OLD LAST_EDUCATION' :", end=" ")
                OLD_LAST_EDUCATION = input()
                LOC_LAST_EDUCATION = STUDENT_LAST_EDUCATION.index(
                    OLD_LAST_EDUCATION)

                print("ENTER 'NEW LAST_EDUCATION' :", end=" ")
                NEW_LAST_EDUCATION = input()
                STUDENT_LAST_EDUCATION[LOC_LAST_EDUCATION] = NEW_LAST_EDUCATION
                print("\t 'LAST_EDUCATION UPDATED SUCCESSFULLY.")
                print("\n")

    @staticmethod
    #    THIS FUNCTION HELP TO UPDATE 'DATA' OF STUDENT.
    def DISPLAY_STUDENT_INFORMATION():
        print("DISPLAYING STUDENTS INFORMATION : \n")

        if len(STUDENT_NAME) == 0 and len(STUDENT_ID) == 0 and len(STUDENT_AGE) == 0 and len(
                STUDENT_SEX) == 0 and len(STUDENT_FATHER_NAME) == 0 and len(STUDENT_MOTHER_NAME) == 0 and len(
                STUDENT_LAST_EDUCATION) == 0:
            print("\n")
            print("\t\t\t 'OOPS ! NOTHING TO DISPLAY, BECAUSE NO DATA IS THERE.")
            print("\n")
        else:
            print("STUDENT'S NAME : ", end="\n")

            for x in STUDENT_NAME:
                print(x)
            print()

            print(end="\n")

            print("STUDENT'S ID :", end="\n")

            for y in STUDENT_ID:
                print(y)
            print()

            print(end="\n")

            print("STUDENT'S AGE :", end="\n")

            for z in STUDENT_AGE:
                print(z)
            print()

            print(end="\n")

            print("STUDENT'S SEX :", end="\n")

            for x in STUDENT_SEX:
                print(x)
            print()

            print(end="\n")

            print("STUDENT'S FATHER_NAME :", end="\n")

            for y in STUDENT_FATHER_NAME:
                print(y)
            print()

            print(end="\n")

            print("STUDENT'S MOTHER_NAME :", end="\n")

            for z in STUDENT_MOTHER_NAME:
                print(z)
            print()

            print(end="\n")

            print("STUDENT'S LAST_EDUCATION :", end="\n")

            for x in STUDENT_LAST_EDUCATION:
                print(x)
            print()

            print(end="\n")


SMS = STUDENT_INFORMATION_SYSTEM()

if __name__ == '__main__':
    #   LOGIC OF THE SYSTEM
    print("\n")

    print("\t\t\t\t ' ********** WELCOME TO STUDENT INFORMATION SYSTEM ********** ' \n")
    run = True

    while run:
        print("PRESS FROM THE FOLLOWING OPTION : \n")

        print("PRESS 1 : TO ADD STUDENT INFORMATION.")
        print("PRESS 2 : TO DELETE STUDENT INFORMATION.")
        print("PRESS 3 : TO UPDATE STUDENT INFORMATION.")
        print("PRESS 4 : TO DISPLAY STUDENT INFORMATION.")
        print("PRESS 5 : TO EXIT SYSTEM.")

        OPTION = int(input("ENTER YOUR OPTION : "))
        print("\n")
        print(end="\n")

        if OPTION == 1:
            SMS.ADD_STUDENT_INFORMATION()
        elif OPTION == 2:
            SMS.DELETE_STUDENT_INFORMATION()
        elif OPTION == 3:
            SMS.UPDATE_STUDENT_INFORMATION()
        elif OPTION == 4:
            SMS.DISPLAY_STUDENT_INFORMATION()
        elif OPTION == 5:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
        else:
            print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
            print("\n")
