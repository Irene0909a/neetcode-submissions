# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = Counter(nums)
#         # {1:1, 2:2, 3:3}

#         # if the length of nums = 3 -> [[], [], [], []]
#         # nums = [7,7,8,8] -> [[], [], [7,8]]
#         bucket = [[] for _ in range(len(nums) + 1)]

#         for num, freq in counter.items():
#             bucket[freq].append(num)
        
#         res = []
#         for i in range(len(bucket) - 1, 0, -1):
#             for num in bucket[i]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, freq in counter.most_common(k)]

