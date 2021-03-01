#code demonstrating the difference between sequential, conditional, and repeated steps

#sequential steps
x = 2 #step 1

print ("The value of the variable x is: ", (x)) #step 2

x = x + 2 #step3

print ("The value of the variable x is now: ", (x)) #step 4



#conditional steps
a = 5 #step 1

print ("The valus of the variable a is: ", (a)) #step 2

if a < 10:
    print ("The variable a is smaller than 10") #step 3

if a > 10: 
    print ("The variable a is bigger than 10") #step 4



#repeated steps
n = 5 #step1

print ("The variable n is equal to: ", (n)) #step 2

if n > 0:
    print ("Countdown from: ", (n)) #step 3

while n > 0:
    print (n) #step 4
    n = n - 1 #step 5

print ("Blastoff!") #step 6
