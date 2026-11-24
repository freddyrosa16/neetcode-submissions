class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    target_list.append(i)
                    target_list.append(j)
                    return target_list