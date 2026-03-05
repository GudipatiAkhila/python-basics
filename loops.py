# Loops are used to execute a block of code multiple times.
# In Python, there are two main types of loops:
# for loop
# while loop

# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num) 

# value = 0
# while value <= 10:
#     print(value)
#     value = value+1

# output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# value = 0
# while value <= 10:
#     if value == 6:   # if we like this "continue" it will struck there it self 
#         continue     # so for that we need to add value = value + 1 it will again start looping 
# print(value)
# value = value+1
# #=========================================#
# value = 0
# while value <= 10:
#     if value == 6:
#         value = value + 1   # if we like this "continue" it will struck there it self 
#         continue     # so for that we need to add value = value + 1 it will again start looping 
#     print(value)
#     value = value+1   # continue taruvata it will go above to the while loop
#output
# 0
# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9
# 10

#** ====================================================== **
sample = ["server1","server2", "server3","server4"] 
#   for i in sample ====> in --> membership operator it checks whether the element is present or not 
# i --> iterator
# sample --> iterable we are performing action on sample right so it is iterable
# for i in sample:
#     print(i)

#** while loop **
# sample = ["server1","server2", "server3","server4"] 
# i = 0 
# while i < len(sample):
#     print(sample[i])
#     i = i+1

#**=========================================**

# 1) range() is used to generate a sequence of numbers, commonly used in loops.
# 2)range(start, stop, step)
# 3) start → starting number (default = 0)
# 4)stop → ending number (not included)
# 5)step → increment value
print(tuple(range(5)))
for i in range(len(sample)):
    print(sample[i])

#**** ENUMARATE() ******
#enumerate() is used when you want both the index and the value while looping through a list.

for i in range(len(sample)):
    ele = sample[i]
    print(i,ele)
 # output = 0 server1  --- iin the above code we are adding two extra lines to get the code along with indexes instead that we have enumarate function 

# 1 server2
# 2 server3
# 3 server4

for i in enumerate(sample): # using enumarate function we can reduce the lines of code 
    print(i)
# output 
# (0, 'server1')
# (1, 'server2')
# (2, 'server3')
# (3, 'server4')
#* If i want to remove tuple in the above output we can write like this as below
for val, i in enumerate(sample):
    print(val ,i)
# # output 
# 0 server1
# 1 server2
# 2 server3
# 3 server4

