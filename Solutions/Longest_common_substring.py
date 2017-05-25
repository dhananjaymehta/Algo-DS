# longest common substring
# x= "GeeksforGeeks", y = "GeeksQuiz"
# result - Geeks

def method1(str1, str2):
    # brute force - O(n*m^2)
    # generate possible substrings
    comb = []
    l = len(str1)
    for i in range(l):
        for j in range(i, l):
            comb.append(str1[i:j+1])
    # search the substring
    g_str = ""
    for s in comb:
        if s in str2 and len(s)>len(g_str):
            g_str=s
    print(g_str)

def method2(str1, str2):
    # this is an optimized method using:
    # Dynamic programming)
    l_1 = len(str1)+1  # row
    l_2 = len(str2)+1  # col

    # generate a matrix
    matrix = [[0 for i in range(l_1)] for j in range(l_2)]

    # generate count of substring
    for i in range(1,l_2):
        for j in range(1,l_1):
            if str1[j-1]==str2[i-1]:
                matrix[i][j]=matrix[i-1][j-1]+1

    long=(1,1)
    # find the index of longest string:
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]>matrix[long[0]][long[1]]:
                long=(i,j)

    # generate the string:
    res=[]
    i,j = long[0], long[1]
    print("k",i,j)
    while i>0 and j>0:
        res.append(str1[j-1])
        print(res)
        i-=1
        j-=1

    return ''.join(res[::-1])

def method3(st1,st2):
    # this has been further reduced in length
    # creating the matrix
    all_comb = [[0] * (len(st1) + 1) for i in range((len(st2) + 1))]  # width and height
    curr_max = 0
    max_comb_ind=[]

    # going through board to find consec substring letters
    for l in range(1, len(st2) + 1):  # row
        for k in range(1, len(st1) + 1):  # column
            if st1[k - 1] == st2[l - 1]:
                all_comb[l][k] = 1 + all_comb[l - 1][k - 1]
                if all_comb[l][k] > curr_max:
                    curr_max = all_comb[l][k]
                    max_comb_ind = [l, k]
            else:
                all_comb[l][k] = 0
    #print(max_comb_ind, curr_max)
    start_sub_ind = max_comb_ind[1] - curr_max
    end_sub_index = max_comb_ind[1]
    return st1[start_sub_ind:end_sub_index]


#print(max_ov("ftfcatgh", "catra"))
x= "ftfcatgh"
y = "factcatra"
print(method3(st1=x, st2=y))