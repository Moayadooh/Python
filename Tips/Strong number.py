num = int(input("Enter a number : "))

temp = num
sum = 0
while temp>0:
    last = temp % 10
    fact = last
    while last!=1:
        fact = fact * (last-1)
        last = last - 1
    sum = sum + fact
    temp = temp // 10

if sum==num:
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")
