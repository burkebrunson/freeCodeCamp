#the answer to life

x = int ( input("Please enter a number that is the answer to life: "))

if x > 1:
    print ("Your answer is > 1; it may be the answer to life")
    if x < 100:
        print ("Your answer is < 100; it is still possibly the answer to life")
        if x == 42:
            print ("Your answer = 42; it is the answer to life")
print ("All done checking your answer")
