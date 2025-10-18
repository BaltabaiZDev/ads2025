n = int(input().strip())
old_to_new = {}
new_to_old = {}

for _ in range(n):
    old, new = input().split()
    # Егер old бұрын басқа аттан шыққан болса, түпнұсқасын табамыз
    if old in new_to_old:
        origin = new_to_old[old]
        old_to_new[origin] = new
        new_to_old[new] = origin
        del new_to_old[old]
    else:
        old_to_new[old] = new
        new_to_old[new] = old

# Нәтиже шығару
print(len(old_to_new))
for old in sorted(old_to_new.keys()):
    print(old, old_to_new[old])