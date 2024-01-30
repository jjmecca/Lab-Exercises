#Topic 4 $100
class String:
    def __init__(self, string):
        self.string=string
    def remove_left_three(self):
        print(self.string[3:])
a=String("Name of string")
a.remove_left_three()
#Topic 5 $200
#import, false, true, list, return
#Topic 2 $500
#Nothing is printed because the break statement is before the print statement
#Topic 1 $300
#Tuple
#Topic 3 $300
#9
#Topic 2 $200
# += or -=
#Topic 4 $400
#It simply ties things to that particular instance of a class, aka an object
#Topic 5 $300
#It returns an output and stores it.
#Topic 3 $200
#str()
#Topic 3 $400
#Parameters are the rules of a function that you establish when you define a function, arguments are what you plug in when you call a function.
#Topic 1 $200
#float
#Topic 1 $100 - Which data type is surrounded by quotation marks?
#Strings.
#Topic 5 $400 - What is the difference between a local variable and a global variable?
#Global variables are used anywhere in your code while local are only used within a certain scope (ex: functions).
#Topic 2 $300 - Create a basic program that will take a string and count the number of unique characters, storing the results in a dictionary
word = input();
dictionary = {}
for letter in word:
    if letter not in dictionary:
        dictionary[letter]=1
    else:
        dictionary[letter]+=1
print(dictionary)
#Topic 4 $300 - What is the difference a class and an object?
#Objects are an instance of a class. Remember: classes are blueprints for objects.
#Topic 5 $500 - What are some common error messages that Python provides you when coding?
#NameError - variable not found, KeyError - key not in dictionary, TypeError - used function/operation with incorrect data type, SyntaxError - error in your syntax, ImportError - when your imported module can't be found
#Topic 2 $400 - Why would you use a while loop instead of a for loop when writing a program?
#While loops are moreso based on a conditional, while something is true or false. For loops are used when the number of iterations is known.
#Topic 4 $200 - Everything in Python is an object (True/False)
#Topic 1 $400 - Take two lists and write a program that returns a list of their shared numbers. Make sure your new list does not contain duplicates
list_one=[1,1,3,4,9,11,22,33,45,56,98,101,200]
list_two=[1,5,7,9,15,20,33,40,41,45,75,88,99,101]
list_three=[]

for x in list_one:
    for y in list_two:
        if x==y and x not in list_three:
            list_three.append(x)
print(list_three)
#Topic 2 $100 Question - What is this operator called and what does it do? (%)
#It gives you the remainder of a number. (ex: 5%2=1)
#Topic 1 $500 - What dictionary method creates a dictionary when you provide it a list, tuple, or set of keys?
#fromkeys(). Syntax: dict.fromkeys(keys, value)
#Topic 3 $100 Question - What is the syntax for declaring a function?
#"def function_name():" Example:
def AddTwo(a,b,c=None): #When none is used, it creates an optional parameter. 
    return a+b

AddTwo(3,4,5)
AddTwo(3,4)
#Topic 3 $500 - Create a function that takes a string as an argument and automatically (1) checks to see if the string contains all alphabetical characters, (2) casts it as upper case, and (3) if there are more than 5 characters, removes them.
def string_function(string):
    if string.isalpha()==True:
        string=string.capitalize();
        if len(string)>5:
            string=string[:5];
    print(string);
string_function("testing")