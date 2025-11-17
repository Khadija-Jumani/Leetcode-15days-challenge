class Solution:
    def threeSum(self, nums):
        nums.sort()                      # Sort the array
        result = []
        length = len(nums)

        for i in range(length - 2):
            # Skip same element for i to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip same value for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip same value for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1      # Need a larger sum
                else:
                    right -= 1     # Need a smaller sum

        return result
