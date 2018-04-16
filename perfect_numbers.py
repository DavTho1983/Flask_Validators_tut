def classify(num):
    if num == 0:
        return 'not a positive integer. Please input a positive integer'
    factors = []

    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    if sum(factors) > num:
        return 'abundant'
    elif sum(factors) < num:
        return 'deficient'
    return 'perfect'

def listInRange(start, end, aliquot):
    if start >= end:
        return 'You must choose numbers where the start value is less than the end value'

    aliList = []

    for i in range(start, end + 1):
        if classify(i) == aliquot:
            aliList.append(i)

    if aliList == []:
        return 'There are no ' + str(aliquot) + ' numbers in this range'
    return ', '.join(map(str, aliList))
