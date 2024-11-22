class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = N = len(nums)
        first = 0
        while k:
            k %= n
            for second in range(N-k, N):
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
            n -= k
