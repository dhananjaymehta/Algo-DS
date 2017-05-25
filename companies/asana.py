
def getcenter(m,n):
    """
    get possible starting indexes for rabbit.
    :param m: rows of matrix
    :param n: column of matrix
    :return:
        list of all possible center indexes
    """
    if m% 2 == 0 and n % 2 == 1:  # even row, odd col
        return [(m // 2, n // 2), (m // 2 - 1, n // 2)]
    if m % 2 != 0 and n % 2 == 0:  # odd row, even col
        return [(m // 2, n // 2), (m // 2, n // 2 - 1)]
    if m % 2 == 0 and n % 2 == 0:  # even row, even col
        return [(m // 2, n // 2), (m // 2, n // 2 - 1), (m // 2 - 1, n // 2), (m // 2 - 1, n // 2 - 1)]
    else:  # odd row, odd col
        return [(m // 2, n // 2)]


def getstartindex(m, n, nums):
    """
    get the starting index for rabbit
    :param m: rows of matrix
    :param n: column of matrix
    :param nums: m X n matrix 2D matrix representing the garden
    :return:
        (row,column): tuple of starting index for the rabbit
    """
    start = getcenter(m, n)  # call function getcenter(m,n) to get probable starting indexes
    center = start[0]
    max_dist = nums[center[0]][center[1]]
    for i in range(1, len(start)):
        temp = nums[start[i][0]][start[i][1]]
        if temp > max_dist:
            center = (start[i][0], start[i][1])
    return center


def helper_data(r, c, nums):
    """
    detect if corners of the matrix
    :param r: row of the matrix
    :param c: column of the matrix
    :param nums: m X n matrix 2D matrix representing the garden
    :return:
        nums[r][c]: value at the index r,c
    """
    if r < 0 or c < 0 or r > len(nums)-1 or c > len(nums[0])-1:
        return 0

    return nums[r][c]


def helper(r, c, nums, result):
    """
    help rabbit to navigate to next index with maximum carrots in the matrix
    :param r: starting row
    :param c: starting column
    :param nums: m X n matrix 2D matrix representing the garden
    :param result: total carrots eaten by rabbit
    :return:
        result : carrots eaten by rabbit
    """
    if r < 0 or c < 0 or r > len(nums)-1 or c > len(nums[0])-1:
        return result

    next_center = (r + 1, c)  # check down
    max_point = helper_data(r + 1, c, nums)

    temp_max = helper_data(r - 1, c, nums)  # check up

    if temp_max > max_point:
        next_center = (r - 1, c)
        max_point = temp_max

    temp_max = helper_data(r, c - 1, nums)  # check left
    if temp_max > max_point:
        next_center = (r, c - 1)
        max_point = temp_max

    temp_max = helper_data(r, c + 1, nums)  # check right
    if temp_max > max_point:
        next_center = (r, c + 1)
        max_point = temp_max

    if max_point == 0:
        return result  # if all surrounding values are zero
    else:
        nums[r][c] = 0  # set current value to zero if traversed
        return helper(next_center[0], next_center[1], nums, result + max_point)


def main(nums):
    """
    :param nums: m X n matrix 2D matrix representing the garden
    :return:
        result: total number of carrots eaten by Rabbit till all nearby carrots are eaten
    """
    center = getstartindex(len(nums), len(nums[0]), nums)  # get starting index for rabbit
    return helper(center[0], center[1], nums, nums[center[0]][center[1]])


# Test Cases:
# ---------------
# Case 1: nums = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]] -> 27
# Case 2: nums = [[5, 7, 8, 6, 3], [0, 0, 2, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]] -> 17
# Case 3: nums = [[5, 7, 8, 6, 3], [0, 0, 2, 0, 4], [4, 6, 3, 12, 9], [12, 1, 0, 5, 8]] -> 37
# Case 4: nums = [[5, 7, 8, 6], [0, 0, 2, 0], [4, 6, 3, 12], [12, 1, 0, 5]] -> 23
# Case 5: nums = [[5, 7, 8], [0, 0, 2], [4, 6, 3], [12, 1, 0]] -> 23
# Case 6: nums = [[5, 7], [0, 0], [4, 6], [12, 1]] -> 23
# Case 7: nums = [[4, 6],[12, 1]] -> 23
# Case 8: nums = [[4, 6, 3]] -> 10
# Case 9: nums = [[4, 6]] -> 10
# Case 10: nums = [[4]] -> 4
nums = [[4]]

#nums = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]]  # test case 1
carrots = main(nums)  # call main function to get total carrots
print(carrots)