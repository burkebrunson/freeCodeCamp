#more conditional structures: if, and if/then/else

#multi-way branch
x = float (input ("Please provide a number for x: "))
"""
Order matters; at least one of these statements will run
"""
if x < 2:  #first statement checked; if true, it runs that block and is done
    print ("x is small")
elif x < 10:  #this statement is checked only if first block is false
    print ("x is medium")
else:  #catch-all statement if all others are false
    print ("x is large")
print ("All done")

