class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if nums[i] in seen:
                return [seen[nums[i]], i]
            seen[needed] = i


        