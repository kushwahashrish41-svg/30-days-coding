##Create a program that stores subjects and marks in a dictionary, adds a new subject, and prints the average and highest mark. Handle the empty case without crashing.
## Add three sample entries.
# Initialize the dictionary with sample entries
subjects_marks = {
    "Math": 85,
    "Science": 90,
    "History": 78
}

# Add a new subject and mark
subjects_marks["English"] = 88

# Calculate and print the average and highest mark
if subjects_marks:
    average = sum(subjects_marks.values()) / len(subjects_marks)
    highest = max(subjects_marks.values())
    print(f"Average mark: {average}")
    print(f"Highest mark: {highest}")
else:
    print("No subjects available.")