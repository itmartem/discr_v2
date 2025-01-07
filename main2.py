import sys
import heapq
from collections import Counter
def build_tree(t):
    f = Counter(t)
    h = [(c, s if s is not None else '', None, None) for s, c in f.items()]
    heapq.heapify(h)

    while len(h) > 1:
        l = heapq.heappop(h)
        r = heapq.heappop(h)
        n = (l[0] + r[0], '', l, r)
        heapq.heappush(h, n)
    return h[0]
def generate_huffman_codes(n, p="", m=None):
    if m is None:
        m = {}

    if n[1]:
        m[n[1]] = p
    else:
        generate_huffman_codes(n[2], p + "0", m)
        generate_huffman_codes(n[3], p + "1", m)
    return m
def encode_text(t, m):
    return ''.join(m[c] for c in t)
def decode_text(e, m):
    d = []
    c = ""
    for b in e:
        c += b
        if c in m:
            d.append(m[c])
            c = ""
    return ''.join(d)
def huffman_process(t):
    if not t:
        raise ValueError("Нет текста")

    r = build_tree(t)
    m = generate_huffman_codes(r)
    e = encode_text(t, m)
    d = decode_text(e, {v: k for k, v in m.items()})
    return m, e, d
def main():
    if len(sys.argv) < 2:
        print("Используйте: python3 script.py '<ваш текст>'")
        sys.exit(1)

    t = sys.argv[1]
    m, e, d = huffman_process(t)

    print("\nДекодированное сообщение:")
    print(d)

    print("\nКоды Хаффмана:")
    for s, p in m.items():
        print(f"'{s}': {p}")

    print("\nЗакодированное сообщение:")
    print(e)

if __name__ == "__main__":
    main()
