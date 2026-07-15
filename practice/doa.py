from sys import stdin


# Hilfsfunktion, die 2D-Feld ausgibt.
def printM(M, n, m):
    for i in range(n):
        for j in range(m):
            print(M[i][j], end="\t")
        print()


# Parsing
tokens = iter(stdin.read().split())

N = int(next(tokens))
L = int(next(tokens))

A = [None for _ in range(N)]
B = [None for _ in range(N)]

for i in range(N):
    A[i] = int(next(tokens))

for i in range(N):
    B[i] = int(next(tokens))

# Algorithm: DP-Tabulation mit L + 1 * N + 1 Feld.
S = [[None for _ in range(L + 1)] for _ in range(N + 1)]

# Zustände (i, j) in (N, L) mit Werten: Summe, Anzahl Tausche, und derzeitiger Index (A oder B) in Lösung.
# Randfälle:
# i = 0 -> S = 0
# j = 0 -> S = sum(A)

for j in range(L + 1):
    S[0][j] = (0, 0, 0)

for i in range(N + 1):
    S[i][0] = (sum(A[:i]), 0, 0)

# Rechenregel wenn alle möglichen Tausche möglich sind:
# S[i][j] = max(S[i-1][j] + A[i-1], S[i-1][j] + B[i-1], S[i-1][j-1] + A[i-1], S[i-1][j-1] + B[i-1])
#         = max(S[i-1][j], S[i-1][j-1]) + max(A[i-1], B[i-1])

for j in range(1, L + 1):
    for i in range(1, N + 1):
        # Tausch immer unnötig
        EQ = A[i - 1] == B[i - 1]

        # Maximum von neuem A und B
        MAB = max(A[i - 1], B[i - 1])

        # Wir gehen von links oben nach rechts -> mindestens ein Tausch immer möglich
        C1 = S[i - 1][j - 1][0] + MAB
        C1_S = 0
        C1_i = S[i - 1][j - 1][2]  # Feld in dem sich dieser Kandidat derzeit befindet.
        # Mussten wir tauschen für MAB?
        if not EQ and MAB != (A, B)[C1_i]:
            C1_S = 1
            C1_i = (C1_i + 1) % 2

        # Wir gehen von oben nach unten -> Tausch nur möglich, wenn genug übrig!
        C2 = S[i - 1][j][0]
        C2_S = 0
        C2_i = S[i - 1][j][2]  # ...
        if S[i - 1][j][1] < j and not EQ and MAB != (A, B)[C2_i]:
            C2 += MAB
            C2_S = 1
            C2_i = (C2_i + 1) % 2
        else:
            # Wenn kein Tausch möglich oder nötig ist, addiere das nächste Element
            C2 += (A, B)[C2_i][i - 1]

        # Tausche nix oder füg etwas hinzu, sondern übernimm einfach das Maximum, was wir für die gleiche Länge aber einen Tausch weniger hatten.
        C3 = S[i][j - 1][0]
        C3_i = S[i][j - 1][2]

        # Priorisiere C3, dann C2, und zuletzt C1, um die Tauschanzahl zu minimieren.
        if C3 >= C2 and C3 >= C1:
            S[i][j] = (C3, S[i][j - 1][1], C3_i)  # Behalte die Tauschanzahl und Index.
        elif C2 >= C3 and C2 >= C1:
            S[i][j] = (C2, S[i - 1][j][1] + C2_S, C2_i)  # Wenn getauscht, zähle das!
        else:
            S[i][j] = (C1, S[i - 1][j - 1][1] + C1_S, C1_i)  # ...


# DP-Feld nach Berechnung
# printM(S, N + 1, L + 1)

# Ausgabe
print(S[N][L][0])
