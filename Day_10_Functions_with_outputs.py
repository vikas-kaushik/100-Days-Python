# Function which returns values
def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f'{f_name} {l_name}'

# formatted_name = format_name(f_name='AngELa', l_name='yu')
# print(formatted_name)

# multiple return statements in one function
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name?"), input("What is your last name?")))

# Leap Year
# A year is a leap year if:
# It is divisible by 4 AND
# NOT divisible by 100
# UNLESS it is also divisible by 400

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Call your function with hard coded values
# is_leap_year(2024)

# Docstrings
# Used for documentation
# First line after function def using """XXXX"""

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

# Functions inside functions
def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
# print(result)

#### Calculator ####
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Add the operators and related functions in a dictionary
operation_dict = {
    "+": add, # We are putting function name against operators
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    reuse_last_result = ''
    first_num = float(input('Please enter the first number: '))
    should_accumulate = True
    while should_accumulate:
        for symbol in operation_dict:
            print (symbol)
        operator = input('Please pick an operator: ')
        second_num = float(input('Please enter the second number: '))

        answer = operation_dict[operator](first_num,second_num)
        print(f"{first_num} {operator} {second_num} = {answer}")

        reuse_last_result = input(f'Do you wish to reuse the last result {answer} (y) or start a new calculation? (n): ').lower()
        print(reuse_last_result)
        if reuse_last_result == 'y':
            first_num = answer
        else:
            should_accumulate = False
            print("\n"* 20)
            calculator()

calculator()