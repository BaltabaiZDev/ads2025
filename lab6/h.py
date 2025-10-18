n = int(input().strip())
arr = input().split()
letter = input().strip()

# Іздеу: ең кіші символ, бірақ letter-ден үлкен
for ch in arr:
    if ch > letter:
        print(ch)
        break
else:
    # Егер бәрі <= letter болса, алғашқы символды шығару
    print(arr[0])