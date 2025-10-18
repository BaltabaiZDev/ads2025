n = int(input().strip())
s = input().strip()

# Define vowels
vowels = set("aeiou")

# Separate vowels and consonants
vowel_part = sorted([ch for ch in s if ch in vowels])
cons_part = sorted([ch for ch in s if ch not in vowels])

# Combine
result = "".join(vowel_part + cons_part)

# Output
print(result)