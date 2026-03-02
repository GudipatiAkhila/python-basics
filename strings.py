# strings are immutable datatype 
# by default python stores every strings it treates as a individual component
sample = "This is Akhila"
#print (sample)
sample_1 = "abc" # ("a" ,"b","c") python stores like this by defualt 
#print(dir(sample))

# ""
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# ""
print (sample.capitalize())
print(sample.casefold()) # o/p: this is akhila gives the entire in small letters

print(sample.center(100, "*")) 

# how to reverse a string - imp interview 
print(sample[::-1]) #output: alihkA si sihT

# we can also convert it into tuple and list
print(tuple(sample),list(sample))