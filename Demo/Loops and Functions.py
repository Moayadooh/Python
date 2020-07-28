'''

for value in range(5):  # print from 0 to 5
    print(value)

for value in range(-3,5):  # print from -3 to 4
    print(value)

for value in range(-3,5,2):  # print from -3 to 3 "increase by 2"
    print(value)

name = "Moayad"
for value in name:  # print letter by letter
    print(value)

fruits = ["mango","apple","tomato"]
for value in fruits:
    print(value)

number = 2
for value in range(1,11):
    print(number*value)
'''

number = input("Enter Number ")
for value in range(1,11):  # by default the numbers in range are integers
    multiply = value * int(number)
    line = str(number) + " x " + str(value) + " = " + str(multiply)
    print(line)
'''
i = 0
name = "Moayad"
while(i<5 and name=="Moayad"):  # 'and'   'or'  '1 infinite loop'
    print(i)
    i = i+1
'''
