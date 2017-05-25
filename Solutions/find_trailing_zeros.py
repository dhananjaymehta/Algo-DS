# find Trailing Zeros

def method1(n):
    # this is really naive
    fact = factorial1(n)
    trail = 0
    while fact % 10 == 0:
        trail += 1
        fact //= 10
    return trail

def factorial1(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

def method2(n):
    # this is optimized : find number of 5s
    count=0
    i=5
    while i<=n:
        count+=n//i
        i*=5
    return count

N=100#1171717
print(method2(N))