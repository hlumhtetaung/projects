# Permutation and Combination Revision exercise
from math import factorial
from scipy.special import factorial as sp_factorial

num_list = []
choices = []

# calculate permutation
def permutation(num_list, choices):
    if len(choices) > len(num_list):
        return "The number of choices should be lower than or equal to the number of elements in the list."
    else:
        return sp_factorial(len(num_list)) / factorial(len(num_list) - len(choices))

def combination(num_list, choices):
    if len(choices) > len(num_list):
        return "The number of choices should be lower than or equal to the number of elements in the list."
    else:
        return sp_factorial(len(num_list)) / (factorial(len(choices)) * factorial(len(num_list) - len(choices)))

# Get user input for the numbers in the list
num_count = int(input("Enter the number of elements in the list: "))
for i in range(num_count):
    num = int(input(f"Enter number for position {i + 1}: "))
    num_list.append(num)

# Get user input for the number of choices
choice_count = int(input("Enter the number of choices to select: "))
for i in range(choice_count):
    choice = int(input(f"Enter choice for position {i + 1}: "))
    choices.append(choice)

print(f"The number of possible permutations for the choices {choices} from the list {num_list} is {permutation(num_list, choices)}")
print(f"The number of possible combinations for the choices {choices} from the list {num_list} is {combination(num_list, choices)}")