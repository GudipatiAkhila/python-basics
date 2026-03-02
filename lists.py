server_1 = "172.10.33.25"
server_2 = "172.10.33.26"

servers = ["172.10.33.25","172.10.33.26",True,123,123.67]
#print(type(servers))

#print(type(servers),servers,server_1,server_2)

# I need to get outit get values which are present in the list 
# we can use for index based 
# by default python is index based text
server_1 = servers[0]
#print(server_1)
# I want provide some text before IP address like "my IP address is this..etc"

#print("server 1 IP address:", server_1)
server_2 = servers[-1]
#print(server_2)

# if i want first and second index for that we have slicing concept
# slicing (start_index:end_index)
# as end index in python is not inclusive 
simple_slice = servers[0:2]
#print(simple_slice) 
# in the above print statement it will print only 0th index value only even though we mentioned 1 but it will not print 
# slicing (start_index:end_index + 1)
simple_slice = servers[0:1]
#print(simple_slice) 

servers = ["172.10.33.25","172.10.33.26",True,123,123.67,345.4]
simple_slice = servers[0:5:2]
#print(simple_slice)
# slicing (start_index:end_index:Step_size) 
simple_slice = servers[1:6:2] #[1 , 1+2 , 3+2,5+2 ]
#print(simple_slice)

# python also supports negative indexing also 
# negative indexing

servers = ["172.10.33.25","172.10.33.26",True,123,123.67,345.4]
simple_slice = servers[-1:-4:-1] # -1, -1-1 -2-1,-3-1
simple_slice = servers[-1:-5:-1]
#print(simple_slice)  

# To know the length of list - use len() function 
#print("lenght of list:" , len(simple_slice))

# list is a mutable datatype
# mutable: once defined , can change at any time : list , dictionaries 
#immutable : once defined can't be chnaged  : Tuple , sets 

#print("before modify:", servers)
servers[-3] = 12345
#print("after modification:", servers)

#print ("list of operations:", dir(servers))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

servers = ["172.10.33.25","172.10.33.26",True,123,123.67,345.4]
print("Before:" , servers)
servers.append(True)
print("After:",servers)

# we can also attach list also 
servers.append(["a","b"])
print(servers)
#This is the output for above statement ['172.10.33.25', '172.10.33.26', True, 123, 123.67, 345.4, True, ['a', 'b']]
# If I want to get out last a,b so for that 

print(servers[-1])
servers.append(['a','b'])
print("after append:" ,servers, len(servers))
# append will add the list to the exisitng list like indivial elemts ['a', 'b']

#after append: ['172.10.33.25', '172.10.33.26', True, 123, 123.67, 345.4, True, ['a', 'b'], ['a', 'b']] 9
# multi indexing 
servers.extend(['a','b'])
print("after extend:" ,servers, len(servers))
# extend will add the list to the exisitng list like indivial elemts 'a', 'b'
#after extend: ['172.10.33.25', '172.10.33.26', True, 123, 123.67, 345.4, True, ['a', 'b'], ['a', 'b'], 'a', 'b'] 11

#indexing method 
print(servers.index(123))

# insert method  -
servers.insert(0,2912)
print(servers)
#output : [2912, '172.10.33.25', '172.10.33.26', True, 123, 123.67, 345.4, True, ['a', 'b'], ['a', 'b'], 'a', 'b']

#remove method , It removes first occurence only 
servers.remove(True)
print(servers)

#reverse method  - it will reverse the list 
servers.reverse()
print(servers)

# before output :[2912, '172.10.33.25', '172.10.33.26', 123, 123.67, 345.4, True, ['a', 'b'], ['a', 'b'], 'a', 'b']
#after output: ['b', 'a', ['a', 'b'], ['a', 'b'], True, 345.4, 123.67, 123, '172.10.33.26', '172.10.33.25', 2912]
servers = servers[::-1]
# using this slicing method we get it back the original list 
print(servers)
#output : [2912, '172.10.33.25', '172.10.33.26', 123, 123.67, 345.4, True, ['a', 'b'], ['a', 'b'], 'a', 'b']


#sort , sorted 
servers = 1, 4, 2 , 7,5,6,9,8
servers_1 =sorted(servers)
print(servers_1,servers)
# sorted gives output it will return new list as seen in the below 
#output :[1, 2, 4, 5, 6, 7, 8, 9] (1, 4, 2, 7, 5, 6, 9, 8)


#shallow copy 
servers = ["172.10.33.25","172.10.33.26",True,123,123.67,345.4]
servers_1 = servers.copy()
print(servers_1)
servers_1.remove(123)
print(servers,servers_1)

#interview Questions
"""
1. reverse a list 
2. sort vs sorted
3.integer division vs floor division
4. shallow copy 
5. multi indexing
6. append vs extend
7. mutable vs immutable
8. dir()
"""