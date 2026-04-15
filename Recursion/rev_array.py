class Solution:
    def reverse(self, arr: list, n: int) :
        left = 0
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# calling the function
arr = [1, 2, 3, 4, 5]
n = len(arr)

obj = Solution()
obj.reverse(arr, n)

print(arr)