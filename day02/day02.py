##Write a program that asks for your name, age and favourite subject and prints a formatted sentence,
##then calculates the year you will turn 30. Add comments explaining each line.
##Commit it to your repo in a folder called day02.

name = input("What is your name? ") 
 # Ask the user for their name and store it in the variable 'name'
age = int(input("What is your age? "))
# Ask the user for their age, convert it to an integer, and store it in the variable 'age'
favourite_subject = input("What is your favourite subject? ")
# Ask the user for their favourite subject and store it in the variable 'favourite_subject' 

print(f"Hello {name}, you are {age} years old and your favourite subject is {favourite_subject}.")
# Print a formatted sentence that includes the user's name, age, and favourite subject
year_turn_30 = 2026 + (30 - age)
# Calculate the year the user will turn 30 by adding the difference between 30 and their current age to the current year (2026)
print(f"You will turn 30 in the year {year_turn_30}.")
