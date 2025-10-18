import sys, heapq

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it)); k = int(next(it))

    h = []
    total = 0

    out = []
    for _ in range(q):
        cmd = next(it).decode()
        if cmd == 'insert':
            n = int(next(it))
            if k == 0:
                continue
            if len(h) < k:
                heapq.heappush(h, n)
                total += n
            elif n > h[0]:
                total -= h[0]
                heapq.heapreplace(h, n)  # pop+push
                total += n
            # else: ignore
        else:  # 'print'
            out.append(str(total))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
