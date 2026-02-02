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
    number = int(number)
    factors = []
    if number < 0: number *-1
    for factor in range(1, number+1):
        if number%factor == 0:
            factors.append(factor)
    negF = []
    for factor in reversed(factors):
        negF.append(factor*-1)
    factors = negF + factors
    return(factors)

def greatestCommonFactor(x, y):
    gcf = 0
    fox = allFactors(x)
    foy = allFactors(y)
    for xf in fox:
        if xf in foy and xf > gcf:
            gcf = xf
    if gcf:
        return(gcf)
    else:
        return("there is no common factors")

while True:
    x = input("x: ")
    y = input("y: ")
    z = greatestCommonFactor(int(x), int(y))
    print(z)