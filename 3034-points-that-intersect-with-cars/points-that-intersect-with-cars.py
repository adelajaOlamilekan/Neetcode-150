class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key= lambda num: num[0])
        intervals = [nums[0]]

        for index, value in enumerate(nums):
            if index == 0:
                continue
            if value[0] <= intervals[-1][1]:
                max_value = max(intervals[-1][1], value[1])
                intervals[-1][1] = max_value
            else:
                intervals.append(value)
        
        sum_car = 0
        for value in intervals:
            sum_car += value[1] - value[0] + 1
        
        return sum_car
        