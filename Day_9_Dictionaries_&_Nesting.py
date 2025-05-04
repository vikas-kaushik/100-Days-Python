# Python dictionaries are key/value pairs

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

# Adding a new key/value pair OR editing the value for an existing key
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Empty dictionary
empty_dict = {}

# looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades.
#
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
#
# The final version of the student_grades dictionary will be checked.
#
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.
#
# This is the scoring criteria:
#
# - Scores 91 - 100: Grade = "Outstanding"
#
# - Scores 81 - 90: Grade = "Exceeds Expectations"
#
# - Scores 71 - 80: Grade = "Acceptable"
#
# - Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
grade = ''
for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        grade = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        grade = "Acceptable"
    elif student_scores[key] <= 70:
        grade = "Fail"

    student_grades[key] = grade
print(student_grades)


# Nested Lists and Dictionaries

# my dict = {
#     key 1 : [List],
#     key2: {dict}
# }

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# print Lille
print(travel_log["France"][1])

# print "D"
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[-1][1])


# Nested dictionary in a dictionary
# print Stuttgart
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][-1])

#### Silent Auction ####
# DO-1: Ask the user for input
bidder_dict = {}
while True:
    bidder_name = input("What is your name? : ")
    bid_amt = int(input("What is your bid? : $"))

# DO-2: Save data into dictionary {name: price}
    bidder_dict[bidder_name] = bid_amt

# DO-3: Whether if new bids need to be added
    add_more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if add_more_bidders == 'yes':
        print("\n" * 100)
    else:
        break

# DO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bidder= ''
    highest_bid = 0
    for key in bidding_dictionary:
        if bidding_dictionary[key] > highest_bid:
            highest_bid = bidding_dictionary[key]
            highest_bidder = key

    print(f"The winner is {highest_bidder} with a bid amount of ${highest_bid}")

find_highest_bidder(bidder_dict)

