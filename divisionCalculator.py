stringNumerator = input("what is your numerator? ")
numerator = float(stringNumerator)
stringDenominator = input("what is your denominator? ")
denominator = float(stringDenominator)
    
result = numerator / denominator

def printResults():
    print("the result is", result)
    if numerator%denominator == 0:
        print("denominator divides numerator with no remainder (remainder = 0)")
    else:
        print("result is", result, "and remainder is", remainder)

if (numerator / denominator) > 0:
    remainder = (numerator / denominator) - (numerator // denominator)
    printResults()
if (numerator / denominator) < 0:
    remainder = -(numerator / denominator) - ((-1 * numerator) // denominator)
    printResults()
if (numerator / denominator) == 0:
    print("the result is 0. there is no remainder.")
    
#this code does not work for 8/6 because remainder should be 2 not 1
#need to modify so that remainder is multiplied by HCF