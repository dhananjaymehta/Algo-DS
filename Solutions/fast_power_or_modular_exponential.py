# Fast modular exponentiation
# e.g. a^2 % b ==> ((a%b)*(a%b))%b
# e.g. a^3 % b ==> ((a%b)*(a%b)(a%b))%b
# DP equation : a^n % b ==> (a[n-1]*a%b)%b


def method1(n1, n2, e):
    # this uses tabulation
    if e<1:
        return 1%n2

    prev_exp=[None]*(e)
    prev_exp[0]=n1%n2
    for i in range(1, e):
        prev_exp[i]=(prev_exp[i-1]*prev_exp[0])%n2
    return prev_exp[-1]


def method2(n1, n2, e):
    # this uses memoization - O(n)
    # better than method1 but still out of memory error and time out error
    if e < 1:
        return 1 % n2

    # prev_exp=[None]*(e)
    mod = n1 % n2
    prev=mod
    for i in range(1, e):
        prev = (prev * mod) % n2
    return prev


def method3(a, b, n):
    # this will  have O(lgN)
    # Ref: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation
    ans = 1
    while n > 0:
        print(b, n, a, ans)
        if n % 2 == 1:
            ans = ans * a % b
        a = a * a % b
        n //= 2
    return ans % b


# 1, 2147483647, 2147483647
a=7
b=5
n=201
#print(method3(n1=a,n2=b,e=n))
print(method3(a,b,n))