mySet = set(["apple","orange","banana","orange"])  # will remove repeated words
myValue = set("abcab")  # will remove repeated letters
print(myValue)

firstList = ["ab",65,[5,"Moayad"]]
print(firstList[2][1][:3])


myList = ["Salim",4,"Khalid"]
myList.append("Moayad") # add new item in the list
myList.extend("Ahmed")  # add new item letter by letter
myList.insert(2,"yyy")  # add item in specific position
myList.remove("Moayad")  # remove vale from the list
myList.pop(0)           # remove value by index number
myList.pop(0)
myList.pop(0)
print(myList)
