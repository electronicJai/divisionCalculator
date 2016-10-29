def getNumerator():
    numerator = float(input("what is your numerator? ")) 
    return numerator
def getDenominator():
    denominator = float(input("what is your denominator? "))
    return denominator
def integerCheck(numerator, denominator):
    if int(numerator) == numerator and int(denominator) == denominator:
        return True
    else:
        return False
def computeQuotientNoRemainder(numerator, denominator): 
    quotient = numerator / denominator
    return quotient
def computeQuotientWithRemainder(numerator, denominator):
    if computeQuotientNoRemainder(numerator, denominator) > 0:
        quotient = int(numerator//denominator)
    if computeQuotientNoRemainder(numerator, denominator) < 0:
        quotient = int(numerator//denominator + 1)
    return quotient
def computeRemainder(numerator, denominator, quotient):
    remainder = int(numerator - denominator*quotient) #formula for Euclidian division
    return remainder

def division():
    print("this calculator can compute the quotient and remainder for any real numbers")
    numerator = getNumerator()
    denominator = getDenominator()
    while denominator == 0:
        print("invalid input. division is undefined for denominator = 0.")
        getNumerator()
        denominator = getDenominator()
    if integerCheck(numerator, denominator):
        if numerator%denominator == 0:
            quotient = computeQuotientNoRemainder(numerator, denominator)
            print("your quotient is:", quotient)
            print("these integers are exactly divisible and remainder is 0")
        else:
            quotient = computeQuotientWithRemainder(numerator, denominator)
            remainder = computeRemainder(numerator, denominator, quotient)
            print("your quotient is:", quotient)
            print("your remainder is:", remainder)
    else:
        quotient = computeQuotientNoRemainder(numerator, denominator)
        print("your quotient is:", quotient)
        print("remainder is undefined for division involving non-integers")

division()