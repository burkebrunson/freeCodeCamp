#code to calculate pay

sh = input ("Enter hours: ")
sr = input ("Enter pay rate: ")
fh = float (sh)
fr = float (sr)
#print (fh, fr)
if fh > 40:
    #print ("Overtime")
    rPay = fh * fr
    oPay = (fh - 40.0) * (fr * 0.5)
    #print (rPay, oPay)
    xp = rPay + oPay
else:
    #print ("Regular")
    xp = fh * fr
print ("Pay:", xp)
