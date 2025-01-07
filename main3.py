import sys
#a - элем
#b - показ
#n - степень
#m - mod
def operator(a, b, n, m):
    if n == 0: #a+1
        return (a + 1) % m
    elif n == 1: #a+b
        return (a + b) % m
    elif n == 2: #a*b
        return (a * b) % m
    elif n == 3: #степ
        return pow(a, b, m)
    else:
        result = a
        for _ in range(b - 1):
            result = operator(a, result, n - 1, m)
            if result == 0:
                break
        return result % m

def main():
    if len(sys.argv) != 5:
        print("Запуск python main3.py a b n m")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    n = int(sys.argv[3])
    m = int(sys.argv[4])

    result = operator(a, b, n, m)
    print(f"Гипероператор {n}-ой степени для ({a}, {b}) по модулю {m}: {result}")

if __name__ == "__main__":
    main()
