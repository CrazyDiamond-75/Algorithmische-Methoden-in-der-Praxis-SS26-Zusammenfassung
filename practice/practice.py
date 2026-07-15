# Union Find Linked List Heads
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


# Test Linked List UF with Heads
"""
uf = UF_LL(2)
print(uf.find(1))
uf.union(0, 1)
print(uf.find(1))

exit()
"""


# Union Find Linked List Tails
# Could have been faster for Marry Rich problem, as we only need to find once at the end.
class UF_LL_B:
    class LL:
        def __init__(self):
            self.nxt = None
            self.tail = self
            self.val = None
            self.active = True

        # O(1)
        def __str__(self):
            return "{" + f"{self.val}, ..., {self.tail.val}" + "}"

        # O(n)
        def to_list(self):
            lst = []
            curr = self
            while curr:
                lst.append(curr.val)
                curr = curr.nxt
            return lst

    def __init__(self, size):
        self.sets = [self.LL() for _ in range(size)]
        for i, head in enumerate(self.sets):
            head.val = i

    # O(n)
    def find(self, i) -> LL:
        for head in self.sets:
            if not head.active:
                continue

            curr = head
            while curr:
                if curr.val == i:
                    return curr
                curr = curr.nxt
        return None

    # O(1)
    def union(self, A: LL, B: LL):
        if A is B:
            return
        else:
            A.tail.nxt = B
            A.tail = B.tail
            B.active = False

    # O(n)
    def __str__(self):
        return f"{[head.__str__() for head in self.sets if head.active]}"


# Test Linked List with Tails
"""
uf = UF_LL_B(2)
st1 = uf.sets[0]
st2 = uf.sets[1]
print(uf)
uf.union(st1, st2)
print(uf)
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
