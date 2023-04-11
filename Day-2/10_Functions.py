# some functions are already define such as print, input etc
# here the user define function for there own task
# user deine function

# 01_default function

x='love'
print(x)
print(x)
print(x)

# 02_user define function

def function_name():
    print("you")
    print("you")
    print("you")
function_name()

# 03_ user define function

def umar_age():
    age=input("ENTER umar's age ")
    print(age)
    print(age)
    print(age)
umar_age()

# 04_ user define function

def Umar_love(a):
    print(a)
    print(a)
    print(a)
Umar_love('himself')

# 05 user define function of future age

def future_age ( age):
    
    new_age=age+20
    return new_age
x=future_age(12)
print (x)