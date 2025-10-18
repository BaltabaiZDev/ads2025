import sys, heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, x = data[0], data[1]
    a = data[2:2+n]


    h = [-v for v in a]
    heapq.heapify(h)

    total = 0
    for _ in range(x):
        k = -heapq.heappop(h)
        total += k
        if k > 1:
            heapq.heappush(h, -(k-1))
        else:
            heapq.heappush(h, 0)

    print(total)

if __name__ == "__main__":
    main()
