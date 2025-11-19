class Solution:
    def maxSubArray(self, nums):
        # nums has at least one element (per constraints)
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            # best subarray ending at this element
            current_sum = max(num, current_sum + num)
            # update global best
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum

# Local test (not required on LeetCode)
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(sol.maxSubArray([1]))                      # 1
    print(sol.maxSubArray([5,4,-1,7,8]))             # 23
