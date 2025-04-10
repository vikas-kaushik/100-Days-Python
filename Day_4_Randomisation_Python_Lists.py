import random

# For random integer
random_integer = random.randint(1, 10) #  a<= random_integer <= b
print(random_integer)

# For random float
random_float_0_to_1 = random.random() #  0<= random_float_0_to_1 < 1
print(random_float_0_to_1)

# For random float
random_float = random.uniform(1,10) #  0<= random_float <= 1
print(random_float)

###########################################################################
#Python Lists:

# 1. Lists can have elements of different data types
# 2. fruits = ['Apple','Pear']
# 3. Lists maintain order of data inserted

american_states = ['Delaware', 'NY', 'Texas', 'California']
print(american_states)
print(american_states[0]) # 1st element of list
print(american_states[-1]) # last element of list

american_states[1] = 'New York' # list is mutable
print(american_states)

# add an item to the list
american_states.append("Nevada")
print(american_states)

# add items of a list to another list
american_states.extend(['Florida', 'New Mexico'])
print(american_states)

# Length of a list
print(len(american_states))

# We can have nested lists meaning a list containing multiple lists
list1 = [[1,2,3], [4,5,6,7]]
print(list1)