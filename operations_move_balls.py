"""
Understand.
boxes. '0' empty. 1 => One ball. O(n**2) solution will actually work.

Match: Prefix sum

Plan:
Brute: For each index sum difference between indices of all ones to itself.

If I have distance of all to position 0, I should be able 
 to get for all by subtracting index and leaving or keeping the 1/0

0  0  1  0  1  1
|  |  |  |  |  |
2  1  0  1  2  3
4  3  2  1  0  1
5  4  3  2  1  0

11 8  5  4  3  4

Also... Prefixes for both backward and forward direction
0  0  1  0  1  1
Brute. From every 1, move and front and back and add to moves...
Backwards          Forward                     
2  1  0  0  0  0   0  0  0  1  2  3                     
6  4  2  1  0  0   0  0  0  1  2  4                     
13 8  5  3  1  0                        

Join: 
13 8  5  3  1  0
+  +  +  +  +  +
0  0  0  1  2  4
|  |  |  |  |  |
13 8  5  4  3  4

This gives a good idea of how the prefixing might work...

Backwards             Forwards
0  0  1  0  1  1      0  0  1  0  1  1                       
0  0  2  0  4  5      0  0  3  0  1  0                           

Backwards: Prefixing  Forwards: Prefixing... n - i                            
11 0  0  0  0  0: 3   0  0  0  0  0  4: 2                            
11 8  0  0  0  0: 3   0  0  0  0  2  4: 2                            
11 8  5  0  0  0: 3   0  0  0  1  2  4: 1                            
11 8  5  3  1  0: 2   0  0  0  1  2  4: 1                            
11 8  5  3  1  0: 1   0  0  0  1  2  4: 0                            

... while the increment turns 0 or reaches end.

"""

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        operations = [0] * n
        back_op = front_op = back_ones = 0
        for i in range(n):
            add = int(boxes[i])
            back_op += add * i
            front_op += add * (n - 1 - i)
            back_ones += add

        front_ones = back_ones
        for i in range(n):
            operations[i] += back_op
            back_ones -= int(boxes[i])
            back_op -= back_ones

            operations[n - 1 - i] += front_op
            front_ones -= int(boxes[n - 1 - i])
            front_op -= front_ones

        return operations

"""
Reviewed

Evaluate
Space: O(1) => `operations` is output
Time: O(n)
"""