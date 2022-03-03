my_list = ["salam",25,3,29,35,65]
print(my_list[1])
print(my_list[0])
print(my_list[-1])
print(my_list[1:5])
print('---------------------') #اضافه کردن عنصر هایی ب لیست
odd = [2, 4, 6, 8]
odd[0] = 1 # change the 1st item
print(odd) # Output: [1, 4, 6, 8]
odd[1:4] = [3, 5, 7] # change 2nd to 4th items
print(odd) # Output: [1, 3, 5, 7]
print('---------------------')
odd = [1, 3, 5]
odd.append(7)
print(odd) # Output: [1, 3, 5, 7]
odd.extend([9, 11, 13])
print(odd) # Output: [1, 3, 5, 7, 9, 11, 13]
print('---------------------')
odd = [1, 3, 5]
print(odd + [9, 7, 5]) # Output: [1, 3, 5, 9, 7, 5]
print(["re"] * 3) #Output: ["re", "re", "re"]
print('---------------------') #روش حذف عنصر از لیست
my_list = ['p','r','o','b','l','e','m']
del my_list[2] # delete one item
print(my_list) # Output: ['p', 'r', 'b', 'l', 'e', 'm']
del my_list[1:5] # delete multiple items
print(my_list) # Output: ['p', 'm']
del my_list # delete entire list
print('---------------------')
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = [] # ['p', 'r', 'b', 'l', 'e', 'm']
my_list
my_list[2:5] = [] # Output: ['p', 'r', 'm']
print(my_list)
print('---------------------') #بررسی عضویت یک عنصر در لیست
my_list = ["'p','r','o','b','l','e','m’"]
print('p' in my_list) # Output: True
print('a' in my_list) # Output: False
print('c' not in my_list) # Output: True