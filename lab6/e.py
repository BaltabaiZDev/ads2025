n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Бағандарды кему ретімен сұрыптау
for c in range(m):
    col = [matrix[r][c] for r in range(n)]
    col.sort(reverse=True)
    for r in range(n):
        matrix[r][c] = col[r]

# Шығаруда әр элементтен кейін бос орын болуы тиіс
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()