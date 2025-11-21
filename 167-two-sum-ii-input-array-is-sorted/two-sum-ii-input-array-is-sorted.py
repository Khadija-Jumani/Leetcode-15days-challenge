class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # If the sum matches target → return 1-indexed positions
            if current_sum == target:
                return [left + 1, right + 1]

            # If sum is too small → move left pointer forward
            elif current_sum < target:
                left += 1

            # If sum is too large → move right pointer backward
            else:
                right -= 1
