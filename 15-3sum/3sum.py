class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()

        previous_target = -inf
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            target = -1 * nums[i]

            if target != previous_target:
                # print(f"Target{nums[i]}")
                while r > l:
                    # print(target, l, r)
                    if nums[l] + nums[r] == target:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while(l < r and nums[l] == nums[l-1]):
                            l+=1
                    elif nums[l] + nums[r] > target:
                        r -=1
                    elif nums[l] + nums[r] < target:
                        l +=1

                previous_target = target

                # print(f"previous_target {nums[i]}")

        return result


