#expressions

#numeric expressions with operators
#addition +
#subtaction -
#multiplication *
#division /
#power **
#remainder (modulo) %

#precedence - parentheses, power, multiplication/division, addition/subtraction, left-to-right

xx = 2
xx = xx + 2
print ("xx + 2 is: ", xx)

yy = 440 / 12
print ("440 / 12 is: ", yy)

zz = yy / 1000
print ("yy / 1000 is: ", zz)

jj = 23
kk = jj % 5
print ("The remainder of jj / 5 is: ", kk)

print ("The value of 4 raised to the power of 3 is: ", 4 ** 3)

#what does type mean?
#variables, literals, and constants have 'type'
#python knows the difference between integer, number, and string
#i.e. '+' means addition if something is a number and concatenate is something is a string
#we can ask python the type of something by invoking the type function

eee = 'hello'
type (eee)
type ('hello')
type (1)
type (1.0)

#type conversion
print (float(99)+100)
i = 42
type(i)
f = float(i)
print(f)
type(f)

#division in python3 always results in a float result

#you can pass a string of numeric characters to int(), but you cannot pass a string of letters to int()

#python can be instructed to collect data from the user via the input() function; the program will pause and request the info via a prompt to the user
#nam = input ("What is your name? Answer: ")
#print ("Hello, ", nam)
