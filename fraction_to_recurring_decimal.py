"""
Been two weeks...
Understand.
670/333
2 670/333

[0,0,1,2]

Match.
Math. Long Division. Hash map.

Plan.
neg = numerator is -ve
make numerator +ve

keep rem to quotient ordered hash map
it should repeat when the same reminider is reached.

while this is not yet true: rem not in hash map.
    get rem numerator mod denominator
    get quotient numerator int-div denominator
    save rem -> quotient
    new numerator => rem * 10

`rem` is last rem.

create array answer with first key of hashmap as [hashmap[first], '.'] or ['-', [hmfirst], '.']
save the first key as first = (first, hm[first]) - remove it

if number is whole (dict now empty), pop array (remove the '.') and return it joint

Note: if 0 is in the hash map, it means it terminated. not recurring.
For not recurring do like this:
loop though rest of dict and add str(values) to array.

if rem is 0, return joint array answer
add '(' to answer
set is_recurring to False
if first[0] is rem, set is_rec... to True, add first[1] string to answer
go through hashmap, key val.
    if key is rem, set is_rec to true
    if is_rec is true, add val string to answer

add ')' to answer

return joint answer
Implement.
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, d = abs(numerator), abs(denominator)
        fst = r = n % d
        rq = {}
        while r not in rq:
            rq[r] = n // d
            n = r * 10
            r = n % d

        first = rq.pop(fst)
        last = n // d
        decimal = bool(rq or r)
        ans = [f"{'-' * (numerator * denominator < 0)}{first}{'.' * decimal}{"" if r else "".join(map(str, rq.values()))}"]
        if not r: return ans[0]

        recur_start = fst == r
        for k, v in rq.items():
            if recur_start: ans.append('(')
            ans.append(str(v))
            recur_start = k == r

        ans.append(f"{'('*recur_start}{last})")
        return "".join(ans)

"""
Review.
11/2
1: 5, 0: 5 
10 % 2
r = 0
- Last is the repeting so it won't add '('
- Both numer and denom are negative

Evaluate.
Space:
Not counting return value => space of hash map
Worst case: O(denominator)
Cause it could have all possible remainders given that denominator.
i.e. 1 -> denominator - 1. (so O(den.. - 1) which is still O(den..)). Take denominator=7 for example.
but in a terminating fraction (and I think this is an interesting question),
can the long division produce all the possible remainders?

Time:
worst case: O(denominator)
Since that's what it takes to build (and later loop through) the hash map.

Good question.
"""