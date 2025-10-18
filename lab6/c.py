n = int(input().strip())
arr = list(map(int, input().split()))

# Sort the points
arr.sort()

# Find minimum difference
min_diff = float('inf')
for i in range(1, n):
    diff = arr[i] - arr[i - 1]
    if diff < min_diff:
        min_diff = diff

# Collect all pairs with minimum difference
result = []
for i in range(1, n):
    if arr[i] - arr[i - 1] == min_diff:
        result.extend([arr[i - 1], arr[i]])

# Output
print(*result)