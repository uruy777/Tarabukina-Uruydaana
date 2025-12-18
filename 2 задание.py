#1 задание

"""n = int(input())

f = [0, 1]

for i in range(n - 2):
    new_el = f[0] + f[1]
    f[0] = f[1]
    f[1] = new_el

print(f[1])
"""

#2 задание
"""
n = int(input())

ways = [1, 1, 2]

for i in range(n - 2):
    new_el = ways[0] + ways[1] + ways[2]
    ways[0] = ways[1]
    ways[1] = ways[2]
    ways[2] = new_el

print(ways[2])"""

#3 задание
"""
Coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1]
]
Coins = [
    [0, 2, 1],
    [1, 0, 2],
    [2, 1, 0]
    ]

N = 3
M = 3

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue

        elif i == 0:
            Coins[i][j] = Coins[i][j] + Coins[i][j - 1]

        elif j == 0:
            Coins[i][j] = Coins[i][j] + Coins[i - 1][j]

        else:
            Coins[i][j] = Coins[i][j] + max(Coins[i - 1][j], Coins[i][j - 1])

print(Coins[N - 1][M - 1])
"""