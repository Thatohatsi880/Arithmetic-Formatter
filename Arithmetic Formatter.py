from operator import add


def arithmetic_arranger(problems, show):
    if len(problems) > 5:
        print("Error:too many problem")

    arranged_problems = " "


for index, value in enumerate(problems):
    operater = value.split(" ")
if operator(1) not in "+-":
    print("Error: Operator must be '+' or '-' ")

if len(operator[0]) > 4 or len(operator[2]) > 4:
    print("Error: Numbers cannot be more than four digits.")

try:
    number_1 = int(operator[0])
    number_2 = int(operator[2])

except ValueError:
    print("Error: Numbers must only contain digits.")

# calculate the length of each line
addition_values = max(len(operator[0]), len(operator[2]))
width = addition_values + 1
# add spaces to each lne
# line 1
# line 2
number_1 = " "
number_2 = ""
# generate the correct number of dashes below the problem statement
# append the answer if necessary

t_problem = f"""
    {number_1}
    {operator[1]} {number_2}
    """

arranged_problems += t_problems

return arranged_problems