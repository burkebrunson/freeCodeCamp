#code to demonstrate variables, expressions, and statements

#constants - fixed values such as numbers, letters, and strings; string constants use single or double quotes
print (123)
print (98.6)
print ('Hello World')

#reserved words
#False
#None
#True
#and
#as
#assert
#break
#class
#if
#def
#del
#elif
#else
#except
#return
#for
#from
#global
#try
#import
#in
#is
#lamda
#while
#not
#or
#pass
#raise
#finally
#continue
#nonlocal
#with
#yield

#variables - a named place in memory where a programmer can store data and later retrieve the data by using the variable name; contents can change later
x = 12.2
print ("The value of the variable x is: ", x)
x = 14
print ("The value of the variable x is now: ", x)

#sentences or lines
x = 2 #assignment statement; x is variable, = is operator, 2 is constant
x = x + 2 #assignment with expression; x is variable, = and + are operators, 2 is constant
print (x) #print statement; print and parentheses are reserved (print is a built-in function, and we pass it the thing we want to display; parentheses are part of function call); x is variable

#assignment statements
#a variable is a memory location used to store a value; the value stored in a variable can be updated by replacing an old value with a new value
#in an assignment statement, the right side is evaluated before the variable is assigned the value
x = 0.6
x = 3.9 * x * (1 - x)
#the right side is an expression. the expression includes the variable x; so does the left side of the statement.
#this is allowed, because the variable can be reassigned, and because the right side will be done first, then the left side will be done.
#x = 3.9 * 0.6 * (1 - 0.6)
#x = 3.9 * 0.6 * 0.4
#x = 0.936
