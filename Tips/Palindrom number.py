num = int(input("Enter a number : "))

temp = num
sum = 0
while temp>0:
    r = temp % 10
    sum = sum*10+r
    temp = temp // 10

if sum==num:
    print(num,"is a palindrom")
else:
    print(num,"is not a palindrom")
