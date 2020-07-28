value = 0
NumberPass = 0
myList = []

while 1:
    value = value+1
    numTimePass=0
    num = 1

    while num!=11:
        sum = value % num
        num = num+1

        if sum==0:
            numTimePass = numTimePass+1

        if numTimePass==10:
            NumberPass = NumberPass+1
            myList.append(value)

    if NumberPass==2:
            print(myList)
            break
