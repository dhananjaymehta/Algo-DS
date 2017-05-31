# Given a non-negative number represented as an array of digits, plus one to the number.
# [1,2,3] => [1,2,4]
# [9,9,9] => [1,0,0,0]

def plusOne(digits):
    # Write your code here
    carry = 0
    l = len(digits) - 1
    digits[l] += 1
    if digits[l]<10:
        return digits
    for i in range(l, -1, -1):
        digits[i] += carry
        carry = (digits[i]) // 10
        # print(digits[i],carry)
        if carry < 1:
            continue
        else:
            digits[i] %= 10
    if carry:
        digits.insert(0, carry)

    return digits


D=[9,9,9]
print(plusOne(digits=D))