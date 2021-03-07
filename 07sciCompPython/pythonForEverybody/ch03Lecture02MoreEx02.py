#code to calculate pay

sh = input("Enter hours: ")
sr = input("Enter pay rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print ("Error, please rerun program with a numeric input for both prompts")
    quit()

if fh > 40:
    rPay = fh * fr
    oPay = (fh - 40.0) * (fr * 0.5)
    xp = rPay + oPay
else:
    xp = fh * fr
print("Pay:", xp)
