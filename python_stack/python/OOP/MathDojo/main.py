class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self
md = MathDojo()
# # to test:
x = md.add(2).add(2,5,1).subtract(3,2).result

sajeda = md.subtract(4).add(100).result
moh = md.add(70).subtract(50).result
print(moh)
print(sajeda)
print(x)