# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

def coin_change(coins, amount):
    # create matrix
    matrix=[[-1]*(amount+1) for i in range(len(coins))]

    for i in range(len(coins)):
        for j in range(1,amount+1):
            if i==0:
                matrix[i][j]=j//coins[i]
            else:
                # case 1:
                if j<coins[i]:matrix[i][j]=matrix[i-1][j]
                # case 2:
                if j==coins[i]:matrix[i][j]=1
                # case 3:
                if j>coins[i]:
                    if matrix[i-1][j]<0:
                        matrix[i][j]=1+matrix[i][j-coins[i]]
                    else:
                        matrix[i][j]=min(matrix[i-1][j], 1+matrix[i][j-coins[i]])
    return matrix[-1][-1]

C=[1,2,3,4,5]
A=23
#C = [1, 2, 5]
#A = 11
coin_change(coins=C, amount=A)
