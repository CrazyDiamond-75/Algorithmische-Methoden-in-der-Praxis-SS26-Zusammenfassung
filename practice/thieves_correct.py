from sys import stdin


def helper(M, n, m):
    for j in range(m):
        for i in range(n):
            print(M[i][j], end=" ")
        print()


tokens = iter(stdin.read().split())

n = int(next(tokens))
m = int(next(tokens))

entries = [[int(next(tokens)) for _ in range(m)] for _ in range(n)]

# DP[i][j] = Beste Menge an Gold, derzeitige Schlüsselanzahl für Verlauf der bei Stockwerken bis i, und genau j verbrauchten Schlüsseln möglich ist.
DP = [[None for j in range(m + 1)] for i in range(n + 1)]

# Bevor wir anfangen, haben wir kein Gold gesammelt.
DP[0] = [0 for j in range(m + 1)]

# Wenn wir nie Schlüssel hatten, können wir auch nix öffnen.
for i in range(1, n + 1):
    DP[i][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # Nix neues öffnen
        C1 = DP[i - 1][j]

        # Genau eine neue Truhe öffnen, ähnlich wie subset-sum
        C2 = 0
        for k in range(1, j + 1):
            Ck = DP[i - 1][j - k] + entries[i - 1][k - 1]
            if Ck > C2:
                C2 = Ck

        DP[i][j] = max(C1, C2)

        # helper(DP, n + 1, m + 1)
        # print("----------------")
print(max(DP[n]))
