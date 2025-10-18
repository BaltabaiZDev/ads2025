n = int(input().strip())

# Read all dates
dates = [input().strip() for _ in range(n)]

# Convert to sortable tuples (year, month, day)
parsed = []
for d in dates:
    day, month, year = map(int, d.split('-'))
    parsed.append((year, month, day, d))  # keep original format too

# Sort by (year, month, day)
parsed.sort()

# Print dates in same format
for _, _, _, original in parsed:
    print(original)