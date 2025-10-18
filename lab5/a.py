import sys, heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, *arr = data
    arr = arr[:n]

    # Ерекше жағдай: бір ғана массив болса, шығын 0
    if n <= 1:
        print(0)
        return

    # Min-heap құру
    heapq.heapify(arr)

    total = 0  # long long аналогы, Python int шексіз
    while len(arr) > 1:
        a = heapq.heappop(arr)  # ең кішісі
        b = heapq.heappop(arr)  # келесі кішісі
        s = a + b               # осы біріктіру құны
        total += s
        heapq.heappush(arr, s)  # жаңа ұзындықты қайта саламыз

    print(total)

if __name__ == "__main__":
    main()
