#functions - store and reuse of code by defining a function
#any time you use the print command, you are actually invoking a python function
#print() is a built-in function already defined in python
#we can extend python's functionality by defining our own functions and
#"calling" them using the same invocation. we pass the function information
#to process by putting an argument in the parentheses during a function call.
#the infoamtion is passed to a defined function, because there will be
#parameters contained in the parentheses after the same of the fuction.

#a function to print a welcome message to a named user
def hello(n):
    print ("Hello,", (n))

#ask for the user's name
name = input ("Please enter your name: ")

#print the user's name
hello (name)
print ("End of program")
