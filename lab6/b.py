n, m = map(int, input().split())

# Read arrays
a = list(map(int, input().split())) if n > 0 else []
b = list(map(int, input().split())) if m > 0 else []

# Count occurrences
from collections import Counter

count_a = Counter(a)
count_b = Counter(b)

# Find common elements (with repetition)
result = []
for num in count_a:
    if num in count_b:
        # Add each common element min(count_a[num], count_b[num]) times
        result.extend([num] * min(count_a[num], count_b[num]))

# Sort output in order of first appearance from input (optional, but safer)
# Or just sort ascending if needed — examples show sorted order
result.sort()

# Print result
if result:
    print(*result)