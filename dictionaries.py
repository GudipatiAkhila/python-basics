# dictionaries are key : value pair based
# Also known as hashmaps

d = {}
d_1 = dict()

sample = {'a': 1 ,'b': 2}
print (sample['a'])
print(sample.get('b'))
sample = {'akhila':2000,'Akhil': 3000}
print (sample['akhila'])

# keys in dictionaries , once defined can't be chnaged 
# dictionari is immutable datatype 
sample ['a'] = 10 
print(sample)