def reverseInteger(n):
    numR = 0
    ab = None
    if n < 0:
        ab = True
        n = abs(n)

    while n > 0:
        numR = numR * 10 + n % 10
        n //= 10

    # tackle the limit of 32 bit integer result
    if numR < 2147483647:
        if ab:
            return -numR
        else:
            return numR
    else:
        return 0


num=123
reverseInteger(n=num)

