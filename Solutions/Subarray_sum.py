# Given an integer array, find a subarray where the sum of numbers is zero.
# input: [-3, 1, 2, -3, 4], target=0
# return: [0, 2] or [1, 3]
# http://www.geeksforgeeks.org/find-subarray-with-given-sum/
# http://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
def subarry_sum(input, target):
    # mapping={}  # subarray sum mapping
    zero_sum=0
    for i in input:
        zero_sum+=
        if target-i <

def method2(self, nums, k):
    # numbers Sum to k
    # N.O.T.E: for only positive numbers
    if nums is None:
        return 0
    queue = []
    count = 0
    for i in nums:
        queue.append(i)
        tot = sum(queue[:])
        while tot > k and tot != []:
            queue.pop(0)
            tot = sum(queue[:])

        if i == k:
            count += 1
        else:
            if sum(queue[:]) == k:
                count += 1
                # print(queue, sum(queue[:]))
    return count