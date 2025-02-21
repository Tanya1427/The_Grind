"""
Understand.
Easier to find min diff if sorted.
arr.length max 10**5. n**2 won't work.
"Absolute" is a trick. When sorted, diff will always be positive.
When sorted, min diff will always be between two adjacent (think about it).
Distinct. Diff > 0

Match.
Multipass. Sorting.

Plan.
Sort.
Get min diff by checking diff between pairs.
go through pairs and save those that their diff is min diff

(Without multipass would be to map {diff: [a, b]}, and return map[min_diff]
 but two much (double) space in every case (not only worst case))

Implement.
"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))
        return [[arr[i - 1], arr[i]] for i in range(1, len(arr)) if arr[i] - arr[i - 1] == min_diff]

"""
Review.
ed.

Evaluate:
Space: O(n) -> worst case min diff is all diff.
Time: O(nlogn) -> Sorting.
"""