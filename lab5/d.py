import sys, heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    arr = data[2:2+n]

    h = arr[:]
    heapq.heapify(h)

    # Егер бәрі бастаптан-ақ > m болса
    if h and h[0] > m:
        print(0)
        return

    ops = 0
    while len(h) >= 2 and h[0] <= m:
        a = heapq.heappop(h)   # ең кіші
        b = heapq.heappop(h)   # екінші ең кіші
        heapq.heappush(h, a + 2*b)
        ops += 1

    # Қалған ең кішіні тексеру
    if h and h[0] > m:
        print(ops)
    else:
        print(-1)

if __name__ == "__main__":
    main()
