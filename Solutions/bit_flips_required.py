# number of bits required to flip to convert integer N to integer M

def bit_swap(a, b):
    x=a^b
    tot_bit=32
    num=0
    while tot_bit>0:
        if x&1>0:
            num+=1
        x = x>>1
        tot_bit -= 1
    return num
a=9
b=-1
bit_swap(a,b)