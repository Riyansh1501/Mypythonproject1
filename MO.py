import random

num1 = int(input("please tell me a  a random number:/n"))
num2 = int(input("please tell me another -_- number:/n"))


op_list = ["+", "-", "*"]
op = random.randint(0, 2)
if op == 0:
    rhs = num1 + num2

if op == 1:
    rhs = num1 - num2

if op == 2:
    rhs = num1 * num2





rhs = num1 + num2

print("can you tell me the missing operator?(+,-or*):")
answer = input(str(num1) +"__" + str(num2) + " = " + str(rhs) + "\n")
num1

print()


print()

num3 = random.randint(1, 100)

op1=random.randint(0, 1)
op2=random.randint(0, 1)

if op1 == 0:
    rhs = num1 + num2
if op1 == 1:
    rhs = num1 - num2

if op2 == 0:
    rhs = rhs + num3
if op2 == 1:
    rhs = rhs - num3
print("can you tell me the missing operator?(+,-or*):")
answer = input(str(num1) +"__" + str(num2) + " __ " + str(num3) + " = " + str(rhs) + "\n")

