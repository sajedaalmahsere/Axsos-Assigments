class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            right -= 1
            left += 1

        return True


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        digits = []
        temp = x

        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            temp //= 10

        stack = []

        for digit in digits:
            stack.append(digit)

        for digit in digits[::-1]:
            if digit != stack.pop():
                return False

        return True

    stack = []
    num = str(x)
    for(let i = 0; i<num.length; i++){
        stack.push(num[i])
    }
    for(lrt i = 0; i<num.length;i++){
        if(stack.pop() != num[i] ){
            return false;
        }
    }