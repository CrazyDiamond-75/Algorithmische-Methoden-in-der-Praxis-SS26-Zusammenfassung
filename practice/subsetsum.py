inf = float('inf')

def lene(L: list | None):
    if L is None:
        return inf
    else:
        return len(L)

def subsetsum(S: list[int], M: int) -> list[int]:
    # Dynamische Programmierung
    # DP[i][j] := kleinste Teilmenge von S[:i] mit Summe = j <= M
    # Randfälle:
    # DP[0][j] = None, wenn j >= 1
    # DP[i][0] = []
    # Induktionsschritt (rechteres nur wenn S[i] <= j):
    # DP[i][j] = min(key=lene, DP[i-1][j], DP[i-1][j - S[i]] + [S[i]])
    N = len(S)
    DP = [[None for _ in range(M+1)] for _ in range(N+1)] 

    for i in range(N+1):
        DP[i][0] = []

    for i in range(1, N+1):
        for j in range(1, M+1):
            forced = S[i-1] > j
            C1 = DP[i-1][j]
            if forced:
                DP[i][j] = C1
            else:
                C2 = DP[i-1][j - S[i-1]]
                if C2 is not None:
                    C2 += [S[i-1]]
                    DP[i][j] = min(C1, C2, key=lene)
                else:
                    DP[i][j] = C1
                
    print([lene(DP[i][j]) for i, j in zip(range(N+1), range(M+1))])
    return DP[N][M]

print(subsetsum([2, 5, 7, 9, 3, 1], 10))
