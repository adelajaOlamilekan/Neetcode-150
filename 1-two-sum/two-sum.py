class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_number_map = dict()

        for i in range(len(nums)):
            first_number = target - nums[i]
            first_number_index = first_number_map.get(first_number, None)
            if first_number_index != None:
                return [first_number_index, i]
            else:
                first_number_map[nums[i]] = i 
