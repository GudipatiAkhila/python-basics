# what is function 
#A function in python is a block of reusable code that performs a specific task . Functions help make code mpdular , reusable and easier to maintain 
# functions are defined using "def" keyword

def func_name():
    print("hello")
func_name()  # if we couldn't call the function then we didn't get any output 

#===========================================#
# def mult(a,b):
#     return a * b
#a= 6 , b=7 are keyword arguments as they contains keys and vlaues 
# 3, 5 are positional arguments  
# res = mult(3, 5,a=6,b=7)
# print(res)
# output = 
# $ python functions.py
# hello
# Traceback (most recent call last):
#   File "C:\devops\daws-86s\repos\python-basics\functions.py", line 12, in <module>
#     res = mult(3, 5,a=6,b=7)
# TypeError: mult() got multiple values for argument 'a' - so python does not understand how many arguments it should takes.in this case we have a concept call "*args , **kwargs**

#======================================================#
def mult (a, b, *args, **kwargs):
    print(a, b, args, kwargs)
    return a * b
res = mult(3 , 5, 6, 7, c=10, d=12)  #output : 3 5 (6, 7) {'c': 10, 'd': 12} - As we can see this output based on the program we can identify the which values it is [ a, b = 3 5 , args = (6,7) , kwargs = {'c': 10 , 'd': 12}]
# But users don't know the values right so for that we have  --> ""string formating "" 
print(res)
    
#----- * String Formating * ------
def mult (a, b, *args, **kwargs):
    print(f"a:{a}, b:{b}, args:{args}, kwargs:{kwargs}")
    return a * b
res = mult(3 , 5, 6, 7, c=10, d=12) 
print(res) 
#output : a:3, b:5, args:(6, 7), kwargs:{'c': 10, 'd': 12}

def calc(a,b, operation):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a + b
    if operation == "mul":
        return a * b
    if operation == "div":
        return a % b
    
a , b = tuple(map(int , input("Enter two numbers: ").split))
operaton = input ("Enter operation to perform (add, sub, mult,div):")
res = calc(a, b, operation)
print(res)

# when we perform  user input validations first we will split the given input and then we got split function output right that we need to pass an integer  





 