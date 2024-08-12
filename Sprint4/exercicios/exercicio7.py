def pares_ate(n:int):
    return (x for x in range(2, n + 1) if x % 2 == 0)


if __name__ == '__main__':
    print(list(pares_ate(10)))
