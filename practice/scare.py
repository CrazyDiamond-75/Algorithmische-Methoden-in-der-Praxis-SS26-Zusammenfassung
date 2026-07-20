from sys import stdin


# Could be used to even further speed up the algorithm
def countingsort(lst: list[int], maximum=7200):
    counts = [0 for _ in range(maximum)]
    for v in lst:
        counts[v] += 1

    newlst = []
    for v, c in enumerate(counts):
        if c:
            newlst.extend([v for _ in range(c)])
    return newlst


# Parse problem
tokens = iter(stdin.read().split())

n = int(next(tokens))

# Contains ai, bi, si, ti
entries = [
    (int(next(tokens)), int(next(tokens)), int(next(tokens)), next(tokens))
    for _ in range(n)
]

# Idea: We can only pick a movie, if its starting time is 1+last time of a picked movie, or if we remove the last movie.
# Thus, we can compute the right subset of movies, by going through them by time and not index.

# Algorithm, first sort by movie end time.
entries.sort(key=lambda x: x[1])

# Use DP, we want the maximal amount of scares, not an exact amount, thus we don't need the current amount of scares in our state definition. We only need time.

# Maximal shocks based on index of sorted entries
DP = [0] * (n + 1)

# Trivial case, DP[0] = 0

# Inductive case
# Either don't add the ith movie, or remove the last movie, which intersects with the ith movie
# Since we sorted by end time, there can only be one movie, which intersects with the ith movie if it exists at all

for i in range(1, n + 1):
    # Don't pick the movie
    C1 = DP[i - 1]

    # Remove the movie which intersects with the current movie
    j = i - 1
    while j > 0 and entries[j - 1][1] >= entries[i - 1][0]:
        j -= 1

    C2 = DP[j] + entries[i - 1][2]

    DP[i] = max(C1, C2)

print(DP[n])
