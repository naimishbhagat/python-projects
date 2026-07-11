#formula to calculate EMI is : P * R * (1+R)^N / [(i+R)^N - 1]

def emi_calculator(principal,rate,time):
    r = rate/12/100
    emi = (principal * r *(1+r)**time)/((1+r)**time -1)
    return emi

print(emi_calculator(5000000,8.75,240))