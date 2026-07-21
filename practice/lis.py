# LIS PROBLEM
# Input {a_i}_{i \in [n]} \subset \N, n \in \N
# Output: b \subset a such that \forall i \in [|b| - 1]: b_i <= b_{i+1}, and |b| maximal.
#
# Use dynamic programming over input length -> solve for a_0 and then find how to find LIS of a[..i] from a[..i-1]
# DP field DP[i] = length of LIS of a[..i] ending at i
# Base case: DP[0] = 0, DP[1] = 1
# Inductive case: DP[i], we always append to the currently found longest LIS, which we can append to.


def lis(lst: list[int]):
    n = len(lst)
    DP = [0] * (n + 1)

    for i in range(1, n + 1):
        j = max(range(i), key=lambda x: DP[x] if lst[x - 1] <= lst[i - 1] else 0)
        DP[i] = DP[j] + 1

    return max(DP)


print(lis([1, 2, 3, 1, 1, 2]))


def lis_fast(lst: list[int]):
    pass
