class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for x in nums:
            count[x] += 1
            if count[x] > 1:
                return True
        return False

    """
    Thoughts:
    Sorting would help me do it without using memory.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 0
        nums.sort()
        current = nums[0]
        for x in nums:
            if x != current:
                count = 0
                current = x
            count += 1
            if count > 1:
                return True
        return False

