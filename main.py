import math


def f(x_):
    return 1 / math.tan(x_)


if __name__ == "__main__":
    pi = math.pi
    n = 1
    a = pi / 4
    b = pi / 2

    print("\nn\t\t J")

    while n < 1320000:
        h = (b - a) / n
        x = a + h
        sum1 = 0.0
        for k in range(1, n):
            sum1 += 2.0 * f(x)
            x += h

        x = a
        sum2 = 0.0
        for k in range(0, n):
            sum2 += 4.0 * f(x + h / 2.0)
            x += h

        J = h / 6.0 * (f(a) + f(b) + sum1 + sum2)
        print(n, "\t\t", J)
        n = n * 2
