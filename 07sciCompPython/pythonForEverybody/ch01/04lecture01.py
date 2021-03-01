#code to count words in a txt file

#sequential
name = input ("Enter a file: ") #prompt user for file name
handle = open (name, 'r') #open the file provided by user, read it, and put information into variable handle

counts = dict() #creates a dictionary data structure to store word count
#repeated
for line in handle: #for loop to iterate through each word counted in variable handle
    words = line.split() #places each new word in the variable handle into variable words
    for word in words: #for loop to iterate through each new word placed in variable words
        counts[word] = counts.get(word, 0) + 1 #counts the words and stores the count value in dictionary

#sequential
bigCount = None #xreates variable
bigWord = None #creates variable

#repeated
for word, count in counts.items(): #for loop to iterate through each entry in the dictionary counts
    #conditional
    if bigCount is None or count > bigCount: #if statement to determine if variable bigCount is empty or value is less than value of variable count
        bigWord = word #sets variable bigWord equal to value of variable word
        bigCount = count ##sets variable bigCount equal to value of variable count

#sequential
print ("The word repeated the most in the document was: ", (bigWord)) #print bigWord variable info
print ("It was repeated ", (bigCount), " times") #print bigCount variable info
