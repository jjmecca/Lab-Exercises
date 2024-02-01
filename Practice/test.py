#Which data type is surrounded by quotation marks?
#strings
#What is the difference between a local variable and a global variable? - Topic 5 $400
#Global variables are used anywhere in your code while local are only used within a certain scope (ex: functions).
#Loops & $300
#Create a basic program that will take a string and count the number of unique characters, storing the results in a dictionary
word = "mammogram"
dictionary = ""
for i in word:
    if i not in dictionary:
        dictionary += i
print(len(dictionary))