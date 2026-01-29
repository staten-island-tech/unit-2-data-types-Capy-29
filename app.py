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
    for factor in range(1, int(number)):
        if number%factor == 0:
            factors.append(factor)

while True:
    y = input("service: ")
    x = tip(y)
    print(x)