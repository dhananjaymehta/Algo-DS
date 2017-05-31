# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1:1
# 2:2
# 3:n-1+n-2 : 2+1
# 4:n-1, n-2: 3+2
# 5:n-1+n-2: 5+3
# 6:n-1+n-2: 8+5

def method1(n):
    a, b = 1, 2
    res=0
    for i in range(3,n+1):
        res = a+b
        a=b
        b=res
    print (res)

N=5
method1(n=N)