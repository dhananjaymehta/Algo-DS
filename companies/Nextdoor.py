# Dynamic Programming: Maximum number of ways of solving
# Given a score for one team in American football, return each way the team
# could have arrived at that score.
# For simplicity, assume the only ways to score are 2-point safeties, 3-point goals, and 7-point TDs.
# Input: 10
# 0 touchdowns 0 goals 5 safeties
# 0 touchdowns 2 goals 2 safeties
# 1 touchdowns 1 goals 0 safeties
# num_touchdown * TOUCHDOWN + num_goal * GOAL + num_safety * SAFETY = score


def num_to_score(score, ways):
    # This function generates all possible number of scoring the score
    # create a score matrix:
    matrix=[[0]*(score+1) for i in ways]

    # traverse the matrix:
    for i in range(len(ways)):
        for j in range(1,score+1):
            # find ways of making combination
            if i == 0:  # first option
                if j%ways[0] == 0:
                    matrix[0][j]=1
            else:
                if j==ways[i]: matrix[i][j]=matrix[i-1][j]+1    # if match
                elif j< ways[i]: matrix[i][j]=matrix[i-1][j]    # if less than
                else: matrix[i][j]=matrix[i-1][j]+matrix[i][j-ways[i]]

    print(matrix[-1][-1])


num_to_score(15,[2,3,7])

