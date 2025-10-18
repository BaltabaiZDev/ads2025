import sys, heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, *a = data
    a = a[:n]

    # max-heap симуляциясы: салмақтарды теріске айналдырамыз
    h = [-x for x in a]
    heapq.heapify(h)

    while len(h) > 1:
        y = -heapq.heappop(h)  # ең ауыр
        x = -heapq.heappop(h)  # келесі ең ауыр
        if y != x:
            heapq.heappush(h, -(y - x))

    print(0 if not h else -h[0])

if __name__ == "__main__":
    main()
