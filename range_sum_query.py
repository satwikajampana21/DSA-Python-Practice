class RangeSumQuery:

    def __init__(self, arr):
        self.prefix = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            self.prefix[i + 1] = self.prefix[i] + arr[i]

    def sum_range(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


arr = [1, 2, 3, 4, 5]
obj = RangeSumQuery(arr)

print("Range Sum:", obj.sum_range(1, 3))
