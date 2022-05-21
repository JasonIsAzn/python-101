# CH2 
# Jason Le Notes

# Note: Multi-strings are self notes


### Interger and String Values ###

"""
The Basic Data types are Integers(Ints) and Strings
Integers consist of whole numbers that can be zero, pos, or neg, so no fractions
No commas

Strings always contained in single/dobule qoutes
"""
# Integers
print(1)
print(2022) 
print(0) 
print(-1)

# Strings
print("2022")
print("Howdy")
print('howdy')

print(4)
print("4")

print(type(4))
print(type("4"))

# plus operator
print(3 + 2) # addition
print("howdy and " + "gig'em") # string concatenation

print(3 + 5)
print("3" + "5")


# str and int function
print(str(5))
print(int('5'))

print("howdy, " + str(5))
print(1 + int("5"))

# print(int('hello))
# print(int('5.2'))

### Variables and Assignment  ###
"""
The value 10 is binded to a variable called x 
= is called assignmnet operator
x is assigned 10
"""
# basics
x = 10
# illegal: 10 = x


# printing variables
"""automatically prints newline"""
# similar to print('x = ' + 2)
print('x = ' + str(x))
print('x=', x)

# reassignmnet 
x = 5 
print(x)
x = 3
print(x)

# tuple Assignment
""" 
Assign Values Respecively
Does not work if left side is not the same as right side
Tuple is data type similar 
"""
x, y, z = -1, 10 ,25
print (x, y, z)
x, y, z = 5.2, "thisword", 5
print(x, y ,z)

# interesting notes on variables
"""
Show using Boxes and pointers
"""
# ex1
a = 2
b = 3
a = 3
a = 7
# ex2
a = 5
b = 5
# ex3 
x = 2
del x, a, b
#print(x)



### Identifers ###
"""
idenfiters are names for variables
also functions, classes, and methods
"""
# must contain at least on character
#x
# the first character must be alphabetic letter (upper, lower) or and underscore
#mystr
#_str
#str
#Mystr
# the remaing character must be alphabetic letter(upper, lower), underscore, or digit
#my_str
#my_str1
#the_STR
#tHe_St1r2123aD
# can not be a a keyword/reserved word
# Not allowed:
#print
#min
#max 
#def

"""
You'll slowly learn all the common reserved word
If you use a keyword, then your program will break
""" 
#print = 1
#print(2)

""" Case Senseative """
myBirthMonth = 7
mybirthmonth = 6 

print(myBirthMonth)
print(myBirthMonth)

### Floating-Point Numbers ###

"""
Number with decimal precision
Can be neg or pos
"""
print(3.14)
print(-3.15)
print(2.0)

print(6.022e23)
print(2.99e3)
print(2.99E3)

print(round(28.71))
print(round(93.323, 2))
print(round(93.323, 4))
print(round(93.323, -3))

print(int(19.832))
print(type(1.0))
print(type(2))
print(type('2'))


### Control Codes with Strings ###
# All start with an esacpe code
"""
"Normal" Characters are a-b digits and symbols
These are character you can not normally
have in a string
"""
# \' single qoute
print('Jason\'s world ')
print("Jason's World")

# \" double qoute
print("Jason\"s World")
print('Jason"s world ')


# \\ BackSlash
print("BackSlash: \\")
# \n Newline
print("Make Newline \nthis is a newline")

print("Make NewLine")
print("This is a newline")

# \t tab
print("Make a Tab:\thello")
# \b backspace
print("Make a Tab: \bhello")
# \a Alert/Bell
print("Make a Sound: \a ")

### Input ###

#Basic 
x = input()
print(x)

# add text
print("Enter text: ")
x = input() # produce a string value
print("you entered: ", x)
print (type(x))

name = input("Please Enter your Name: ")
print(name)

print("Howdy, Welcome to Python101")
print("Please Enter your Name: ")
#name = input()
print("Printing Name...:", name)

# Demo puasing, functional composition, and problems
x = int(input("Enter Value for x: "))
y = int(input("Enter Value for y: "))

x = float(input("Enter Value for x: "))
y = float(input("Enter Value for y: "))

### Customize Print Function ###
# sep and end

print("howdy", "gigem", "jason", sep= "?")
print("howdy", "gigem", "jason", sep= "????")

print("howdy")
print("and")
print("gig'em")

print("howdy", end='')
print(" and ", end='')
print("gig'em", end='')

print()

#show website python doc

### String Formatting ###
#show website python doc

# default
print("my name is {} and I'm {} years old". format("Jason", 20))
# indexing
print("my name is {0} and I'm {1} years old". format("Jason", 20))
print("my name is {1} and I'm {0} years old". format("Jason", 20))
# variable
print("my name is {name} and I'm {age} years old". format(name ="Jason", age=20))
# alignments
print("{:<5},{:>5}".format(2, 5))
print("{:*<5},{:^>5}".format(2, 5))
print("{:*<5},{:_^25}".format(2, 5))

# signs, percentage and rounding

print("{:.2f}".format(5.1242))

print("{:+d}".format(5))
print("{:+f}".format(5))

print("{:+.2f}".format(5.152423))
print("{:%}".format(1/3))
print("{:.2%}".format(2/3))

print("{:&>+10.2f}, {:_^10}".format(12313122.2342, "hello"))

print("{:,}".format(1231231))

print ("-"*10)
# multistring
"""
can also be ued a multicomments
also called doc string for functions
"""
x =  """cool   
hello
world
wow
"""
print(x)



