# Union Find Linked List
class UF_LL:
    # Linked List
    class LL:
        def __init__(self):
            # Create empty element
            self.top = None
            self.nxt = None
            self.val = None

    def __init__(self, size):
        self.sets = [LL() for _ in range(size)]
        for i, ll in enumerate(self.sets):
            ll.top = ll
            ll.val = i

    # O(1)
    def find(self, i):
        return self.sets[i].top.val

    # O(n)
    def union(self, i, j):
        head1 = self.sets[i]
        head2 = self.sets[j]

        curr = head2
        while curr:
            curr.top = head1.top
            curr.val = i
            curr = curr.nxt


# Test Linked-List UF
"""
uf = UF_LL(2)
print(uf.find(1))
uf.union(0, 1)
print(uf.find(1))

exit()
"""


# Union find using dictionaries
class UF_DICT:
    def __init__(self, size):
        self.dict = {
            i: i for i in range(size)
        }  # Stores index for each element of a set

    # O(1) on average, worst case O(n)
    def find(self, i):
        return self.dict[i]

    # O(n)
    def union(self, i, j):
        for val in self.dict.keys():
            if self.dict[val] == j:
                self.dict[val] = i


# Test Dictionary UF
"""
uf = UF_DICT(2)
print(uf.find(1))
uf.union(0, 1)
print(uf.find(1))

exit()
"""
