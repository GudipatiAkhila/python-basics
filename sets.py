# sets are unordered collection 
# sets removes duplicates and stroes unique values 
sample =  {'akhila', 'akhila2','akhila'}
print(sample)
# output : {'akhila2', 'akhila'} - it removes duplicated gives an unique values only .
#print(dir(set))

# these following methods 
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#1): add method
s1 = {1,2,3,3,4,4,5}
s2 = {2,3,4,8,9,1,6}
s1.add(10)
s2.add(9)
print(s1)   # {1, 2, 3, 4, 5, 10}  we can observe here removes repated values like 3 , 4 gives us unique values 
print(s2)   # {1, 2, 3, 4, 6, 8, 9}

#2) clear() - removes all elements
s = {1,2,3}
s.clear()
print(s) # o/p: set()

# 3) copy() - creates a shallow copy 
s1 = {'akhila','dad','mom' }
s2 = s1.copy() 
print(s2)  # {'mom', 'dad', 'akhila'}

# 4) difference() - it returns elements present in the first set but not in second 
a = {1,2,3}
b = {2,3,4}
print(a.difference(b)) # ouput : {1}

# 5): difference_update() - removes common elements (updates original set()) 
a = {1,2,3,4,5,6,7}
b = {2,3,4,5,6,7}
print(a.difference_update(b))