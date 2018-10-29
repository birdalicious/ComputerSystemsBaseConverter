def toDigits(n, b):
    """Convert a positive number n to its digit representation in base b."""
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    return digits

def fromDigits(digits, b):
    """Compute the number given by digits in base b."""
    n = 0
    for d in digits:
        n = b * n + d
    return n

def convertBase(digits, b, c):
    """Convert the digits representation of a number from base b to base c."""
    return toDigits(fromDigits(digits, b), c)

def convert(n, a, b):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = n//10
    digits = digits[::-1]
    digits = "".join([str(i) for i in convertBase(digits, a, b)])
    if digits == "":
        return 0
    else:
        return int(digits)