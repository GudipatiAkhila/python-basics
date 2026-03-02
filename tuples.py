t = ()
t1 = tuple()

sample = ("172.10.33.25", "172.10.33.26", True, 123, 1234.56, 1234.567)
print(type(sample), sample)
print(sample[0])
print(sample[0:6])
print(sample[-6:])


print(dir(tuple))

# "
# 'count', 'index' "
# These are the two methods in the tuple 

sample = (1,2,3,4,5,5,6)
print(sample.count(5),sample.count(12))
print(type(sample))
print(sample.index(5))

#Data type conversion
sample = ("172.10.33.25", "172.10.33.26", True, 123, 1234.56, 1234.567)
sample_1 = list(sample) #  we can change the tuple datatype to list also 
print(type(sample_1)) 

sample_t = tuple(sample_1)
print(type(sample_t))