# dictionaries are key : value pair based
# Also known as hashmaps

d = {}
d_1 = dict()

sample = {'a': 1 ,'b': 2}
print (sample['a'])
print(sample.get('b'))
sample = {'akhila':2000,'Akhil': 3000}
print (sample['akhila'])

# we can also include tuple in dictionari in the below ("a", "b")- is tuple
sample = {("a" , "b"):1 , 'b': 2}
print (sample)

# keys in dictionaries , once defined can't be chnaged 
# dictionari is immutable datatype 
sample ['a'] = 10 
print(sample)

print(dir(dict))

#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
print(sample.keys(),sample.values()) 
# output : dict_keys([('a', 'b'), 'b', 'a']) dict_values([1, 2, 10])
print(sample.items()) # items gives us complete keys and values output
# dict_items([(('a', 'b'), 1), ('b', 2), ('a', 10)])


#***  convert list to dict ****
sample_list = [ ('a',1) , ('b' , 2)]
sample_dict = dict(sample_list)
print(sample_dict)
