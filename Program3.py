# Program 3: Life stages
# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult
import datetime
while 1:
    age = int(input("Age: "))
    if age < 0:
        print("You cannot have negative age")
    elif age > -1 and age <= 12:
        print ("Kid")
        y = age
        x = 13 - y
        print (f"you need {x} more years before reaching Teen stage")
        break
    elif age >= 13 and age <= 17:
        print("Teen")
        y = age
        x = 18 - y
        print (f"you need {x} more years before reaching Debut stage")
        break
    elif age == 18:
        print("Debut")
        # use single digit only if your birthmonth is single digit only, 
        # ex: January would be 1 instead of 01, same goes with the day
        month = int(input("when is your birth month?: "))
        day = int(input("The day you were born?: "))
        # complete the whole year, ex: 2021
        yearInp = int(input("The year you were born?: "))
        year = yearInp + 19
        bday = datetime.date(year, month, day) - datetime.date.today()
        print(bday)
        break
    else:
        print("Adult") 
        print ("you are already at the final stage")
        break
