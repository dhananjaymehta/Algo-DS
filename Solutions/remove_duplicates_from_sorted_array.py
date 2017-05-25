# Remove Duplicates from Sorted Array
# Note: No extra space


def method1(nums):
    # print(list(dict(collections.Counter(nums)).keys())) -- this take extra space
    prev=0
    for i in range(1, len(nums)):
        if nums[i]!=nums[prev]:
            prev+=1
            nums[prev]=nums[i]

    print(nums[:prev+1])


nums=[1, 1, 1, 1, 1, 1, 1, 2, 2,  2, 2, 2, 2,  2, 2,  2, 2,3]
method1(nums)