# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

#Step 1: Ask for the user's grade
#Step 2: Print the corresponding description and grade/mark
while 1:
    inpGrade = float(input("Input grade: "))
    if inpGrade < 0:
        print ("You cannot input negative number")
    elif inpGrade > 100:
        print ("Your grade cannot exceed 100")
    elif inpGrade <= 74:
        print("Grade/Mark: 5.00")
        print ("Description: Failure")
        break
    elif inpGrade == 75:
        print("Grade/Mark: 3.00")
        print("Description: Passing")
        break
    elif inpGrade <= 78:
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
        break
    elif inpGrade <= 81:
        print("Grade/Mark: 2.50")
        print("Description: Satisfactory")
        break
    elif inpGrade <= 84:
        print("Grade/Mark: 2.25")
        print("Description: Good")
        break
    elif inpGrade <= 87:
        print("Grade/Mark: 2.00")
        print("Description: Good")
        break
    elif inpGrade <= 90:
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
        break
    elif inpGrade <= 93:
        print("Grade/Mark: 1.50")
        print("Description: Very Good")
        break
    elif inpGrade <= 96:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
        break
    elif inpGrade <= 100:
        print("Grade/Mark: 1.00")
        print("Description: Excellent")
        break
