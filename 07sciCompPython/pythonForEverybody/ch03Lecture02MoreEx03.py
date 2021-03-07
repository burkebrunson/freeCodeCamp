def calculatePay(h, r):

    return h * r if h < 40 else ((h - 40) * (r * 0.5) + r * h)


hours = input("Enter Hours : ")

rate = input("Rate : ")
print(calculatePay(float(hours), float(rate)))
