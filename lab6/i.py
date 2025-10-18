# Problem I: Azat likes sorting
s = input().strip()

# Алфавит бойынша сұрыптау (sort қолданбай)
letters = list(s)
n = len(letters)

# Simple bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if letters[j] > letters[j + 1]:
            letters[j], letters[j + 1] = letters[j + 1], letters[j]

print(''.join(letters))