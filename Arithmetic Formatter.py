from codecs import latin_1_decode
from operator import add
from tkinter import N


def arithmetic_arranger(problems, args):
    if len(problems) > 5:
        print("Error:too many problem")

    arranged_problems = [] 

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
        print ("Error: Numbers must only contain digits.")

# calculate the length of each line
addition_values = max(len(operator[0]), len(operator[2]))
width = addition_values + 1
# add spaces to each lne
#result = f"{operator[0]:>{width}}\n{f'{operator[1]} {operator[2]}':>{width}}\n{'-'*width}"

R1 = f"{operator[0]:>{width}}"
R2 = operator[1] + f"{operator[2]:>{width-1}}"
d = '-' * width


try:
   arranged_problems[1] += ('' * 4) + R1
except IndexError:
     arranged_problems.append(R1)

try:
   arranged_problems[2] += ('' * 4) + R2
except IndexError:
     arranged_problems.append(R2)

try:
   arranged_problems[3] += ('' * 4) + d
except IndexError:
     arranged_problems.append(d)


if args:
   """
   This runs if the second parameter True is
   passed in denoting we need to calculate
   the answer value.
   """
      answer = f"{int(operator[0]) + int(operator[2]):>{width}}"
      if operator[1] == '+' else: int(operator[0]) - int(operator[2])
a = f'{str(answer):<{width}}'


try:
     arranged_problems[3] += ('' * 4) + a
except IndexError:
     arranged_problems.append(a)

  
#print(f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}")
r_output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems}[2]\n{arranged_problems[3]}"
r_output = r_output + f"\n arranged_problems[3]"
if args else r_output
return output
