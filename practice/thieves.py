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

# DP[i][j] = Beste Menge an Gold, derzeitige Schlüsselanzahl für Verlauf der bei Stockwerken bis i, Truhen bis j endet.
DP = [[None for j in range(m + 1)] for i in range(n + 1)]

# Bevor wir anfangen, haben wir genau m Schlüssel übrig.
DP[0] = [(0, m) for j in range(m + 1)]

# DP[i][0] repräsentiert für i > 0 die Fälle, bei denen wir uns dazu entscheiden keine Truhe im Stockwerk i zu öffnen.

for i in range(1, n + 1):
    for j in range(m + 1):
        # Derzeitiger Knoten hat Kosten j, Wert 0, wenn j = 0, sonst entries[i-1][j-1]
        # Totales Gold, übrige Schlüssel = DP[i][j]

        # Finde bestmöglichen Vorgänger, der sich j noch leisten kann.
        gmax = -1
        smax = -1
        for k in range(m + 1):
            g, s = DP[i - 1][k]
            if s >= j and (g > gmax or (g == gmax and s > smax)):
                gmax = g
                smax = s

        # Wenn wir das Stockwerk überspringen wollen, dann wollen wir auch kein Gold!
        newgold = 0 if j == 0 else entries[i - 1][j - 1]

        if gmax == smax == -1 and j != 0:
            DP[i][j] = None
        else:
            DP[i][j] = (gmax + newgold, smax - j)

        helper(DP, n + 1, m + 1)
        print("------------------------")


# Problem: Zustandsdefinition ist leider nicht gut genug, es kann sein, dass eine Truhe später irgendwo vorkommt, die man sich nie mehr leisten könnte mit den Entscheidungen, die zuvor getroffen wurden.
