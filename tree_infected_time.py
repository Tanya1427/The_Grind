# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand:
You don't want to actually infect anything.
Maybe you do.
If tree converts to graph, each node can have no more than 3 children
the parent, the left, the right.

Match:
B/D FS. BT. Math. Hashmap

Plan:
Maybe map value: true/false with defaultdict to mark infected
Start from root.

Brute force.
Make tree a graph.
starting from root, map each to it's children - straight forward?
Any way to make it a matrix-represented graph? (with '-' for where cannot be infected?, 'T' for not infected :))

No. Don't do an adjency matrix, it will take too much memory.
Use adjency list.

Not brute force
Make graph from tree using tree's values.
run tree through bfs
Start with root node
pop by levels, associating in the defaultdict like this.
graph[parent].append(child)
graph[child].append(parent)

After having graph, use an "infected" set to track infection
`while` trying to empty a deque.
"""
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        queue = deque([root])
        graph = defaultdict(set)
        childs = ("left", "right")

        while queue:
            node = queue.popleft()  # Could also be dfs 'pop'
            for child in childs:
                child = getattr(node, child)
                if child:
                    graph[child.val].add(node.val)
                    graph[node.val].add(child.val)
                    queue.append(child)

        queue = deque([start])
        infected = {start}
        minutes = 0

        while queue:
            n = len(queue)
            for _ in range(n):
                parent = queue.popleft()
                for child in graph[parent]:
                    if child not in infected:
                        infected.add(child)
                        queue.append(child)

            minutes += 1

        return minutes-1
"""
REVIEWed

EVALUATE:
n=> number of tree nodes
Space: graph O(n->n) | O(n**2) -> nodes
Infected O(n)
queue O(n)
Space: O(n**2)

Time:
Making graph is O(n)
adding to and emptying queue is O(n)

Time: O(n)

Better way.
Start should have it's parent and children as nodes.
Find max distance from start to last leaf node.
Done.

"""