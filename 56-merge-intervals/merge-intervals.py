class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        ans = [intervals[0]]

        for index, value in enumerate(intervals):
            print(value)
            if index == 0:
                continue
            if value[0] <= ans[-1][1]:
                max_value = max(value[1], ans[-1][1])
                ans[-1][1] = max_value
            else:
                ans.append(value)
        return ans

        