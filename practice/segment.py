from collections.abc import Callable as func


def parent(i):
    return (i + 1) // 2 - 1


def children(i):
    return (2 * i + 1, 2 * i + 2)


# Test
"""
for i in range(100000):
    c1, c2 = children(i)
    assert parent(c1) == parent(c2) == i
"""


class ST:
    def __init__(self, values: list[int], f: func[list[int], int], ne: int):
        """
        Build segment tree from values with function f which has neutral element ne.
        """

        # Store function and neutral element
        self.f = f
        self.ne = ne

        # Find smallest 2^p, such that values fits in extended list.
        p = 0
        while 2**p < len(values):
            p += 1

        # Extend the list with neutral elements
        values = values + [self.ne for _ in range(2**p - len(values))]

        # Create the tree with empty inner nodes, and values as the leaves
        n = len(values)
        self.tree = [None for _ in range(n - 1)] + values
        # Store the intervals associated with each node
        self.intervals = [None for _ in range(n - 1)] + [(i, i) for i in range(n)]

        # Go through all parents in reverse and set their values based on their child values.
        i = n - 2
        while i >= 0:
            c1, c2 = children(i)
            self.tree[i] = self.f([self.tree[c1], self.tree[c2]])
            # Set intervals based on child intervals
            self.intervals[i] = (self.intervals[c1][0], self.intervals[c2][1])
            i -= 1
        return

    def query(self, i, j):
        def query_helper(n):
            l, r = self.intervals[n]
            # If [l, r] ⊆ [i, j] return everything
            if i <= l and r <= j:
                return self.tree[n]
            # If [l, r] ⊆ ¬[i, j] return neutral element
            elif r < i or j < l:
                return self.ne
            # Else there is a non-trivial overlap
            else:
                c1, c2 = children(n)
                return self.f([query_helper(c1), query_helper(c2)])

        return query_helper(0)

    def point_update(self, i, v):
        # length of leaf data
        n = (len(self.tree) + 1) // 2
        # Adjust index to tree node
        i += n - 1

        # Set and backpropagate again
        self.tree[i] = v
        while (
            i := parent(i)
        ) >= 0:  # Infinite loop shouldn't be possible, but safer is safer.
            c1, c2 = children(i)
            self.tree[i] = self.f([self.tree[c1], self.tree[c2]])


# Product of a list
def prod(lst):
    n = 1
    for v in lst:
        n *= v
    return n


# Example test
"""
n = 10
example = list(range(1, n + 1))
st = ST(example, prod, 1)

for i in range(n):
    for j in range(i, n):
        print(i + 1, j + 1, st.query(i, j))
"""

# Point update test
"""
example = [1, 2, 3, 4, 5]
st = ST(example, sum, 0)
print(st.query(2, 4))
st.point_update(2, 9)
print(st.query(2, 4))
"""
