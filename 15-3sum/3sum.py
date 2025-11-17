class Solution:
    def threeSum(self, nums):
        nums.sort()              # Sort the array
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values at i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    # Valid triplet found
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values at left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values at right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1   # Need a bigger sum
                else:
                    right -= 1  # Need a smaller sum

        return result
