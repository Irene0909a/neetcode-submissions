class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            # left = [1, 1, 2, 8]
        
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            # right = [48, 24, 6, 1]
        
        answer = []
        for i in range(n):
            answer.append(left[i] * right[i])
        return answer



