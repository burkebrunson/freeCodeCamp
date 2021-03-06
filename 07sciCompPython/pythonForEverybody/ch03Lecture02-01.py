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

#multi-way puzzles
#which will never print, regardless of the value of x?
#puzzle 1
#if x < 2:
#    print ("Below 2")
#elif x >= 2:
#    print ("Two or more")
#else:  #this line will never be reached; one of two above is always true
#    print ("Something else")

#puzzle 2
#if x < 2:
#    print ("Below 2")
#elif x < 20:
#    print ("Below 20")
#elif x < 10:  #this line will not be reached; line above will also be true
#    print ("Below 10")
#else:
#    print ("Something else")

#try/except structure
#used when a traceback error will likely happen with code as written,
#but we don't want to have that happen; surround it with try
#if the code in the try works, the except is skipped
#if the code in the try fails, the except is engaged

#example
#astr = "Hello Bob"
#istr = int (astr)  #traceback error occurs here, prog stops; can't int a string
#print ("First", istr)

#astr = "123"
#istr = int (astr)
#print ("Second", istr)

#instead, try the code
#astr = "Hello Bob"
#try:
#    istr = int (astr)
#except:
#    istr = -1
#print ("First", istr)

#astr = "123"
#try:
#    istr = int (astr)
#except:
#    istr = -1
#print ("Second", istr)
#if multiple lines are in the try block, whichever line causes error is the last
#line that will be run, along with everything before it; below will be skipped

#real-world example
#i = input ("Enter a number: ")
#try:
#    i = int (i)
#except:
#    i = -1

#if i > 0:
#    print ("Nice work")
#else:
#    print ("Not a number")
