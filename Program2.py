# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

# Step 1, ask the user for 3 inputs
def numInp(order):
    inpNum = float(input("Insert "+  order + " : "))
    return inpNum

firstInp = numInp ("first number")
secondInp = numInp ("second number")
thirdInp = numInp ("third number")

# Make a program to distinguish which input is the lowest
lowest = firstInp
if secondInp < firstInp and secondInp < thirdInp:
    lowest = secondInp
if thirdInp < firstInp and thirdInp < secondInp:
    lowest = thirdInp


print(lowest," is the lowest number value")