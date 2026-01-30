def oddOrEven(value):
    if value%2 == 0:
        return "Even"
    else:
        return "Odd"

def tip(service):
    if service == "bad":
        return(0)
    if service == "okay":
        return(15)
    if service == "good":
        return(20)
    if service == "great":
        return(25)

def allFactors(number):
    factors = []
    if number < 0: number *-1
    for factor in range(1, int(number)+1):
        if factor:
            if number%factor == 0:
                factors.append(factor)
    factors = reversed(factors) + factors
    return(factors)

def greatestCommonFactor(x, y):
    gcf = 0
    fox = allFactors(x)
    foy = allFactors(y)
    for xf in fox:
        for yf in foy:
            if yf == xf and yf > gcf:
                gcf = yf
    if gcf:
        return(gcf)
    else:
        return("there is no common factors")

while True:
    x = input("x: ")
    y = input("y: ")
    z = allFactors(int(x))
    print(z)