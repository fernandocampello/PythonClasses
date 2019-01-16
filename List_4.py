'''this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)'''



'''this_list = ["apple", "banana", "cherry"]
this_list.append(["apple", "banana"])
print(this_list)'''


this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)


this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)


this_list = ["apple", "banana", "cherry"]
for i in range(2):
    this_list.insert(i+1, input("insert the fruit name: "))
print(this_list)
