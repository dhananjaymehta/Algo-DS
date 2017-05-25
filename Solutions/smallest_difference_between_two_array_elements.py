def method1(A, B):
    matrix = [[None] * len(A) for i in range(len(B))]
    #print(matrix)
    min_diff=0
    for i in range(len(B)):
        diff=0
        for j in range(len(A)):
            diff=abs(B[i]-A[j])
            min_diff=min(diff, min_diff)
    return min_diff


def method2(A,B):
    C=[]
    [C.append((x,'A')) for x in A]  # extend the list
    [C.append((x,'B')) for x in B]  # extend the list
    C.sort()  # -- sort the list
    print(C)
    diff=float('inf')
    for i in range(len(C)-1):
        if C[i][1] != C[i+1][1]:
            diff=min(diff, C[i+1][0]-C[i][0])
    print(diff)


A = [3,4,6,7]
B = [2,3,8,9]
method2(A,B)