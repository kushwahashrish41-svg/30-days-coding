##Write or find three small programs with a bug each (an off-by-one, a wrong variable, an unhandled error). Ask your partner to send you theirs. 
##Fix all three and explain each bug in one sentence, including how you found it.
#Here are three small programs with bugs:
#1. Off-by-one error
# Debugging Three Small Programs

# 1. Off-by-One Error

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print(numbers[i])


# 2. Wrong Variable

name = "Shrish"
age = 19

print("Name:", name)
print("Age:", age)


# 3. Unhandled Error

try:
    number = int(input("Enter a number: "))
    print("Double:", number * 2)
except ValueError:
    print("Please enter a valid number.")