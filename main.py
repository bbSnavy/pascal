#!/usr/bin/python3
""" pascal and sierpinski triangle """

even            = lambda n: (n % 2) == 0
odd             = lambda n: not even(n)
pascal_line     = lambda n: [1] if n == 0 else (lambda d: [d.get(x - 1, 0) + d.get(x - 0, 0) for x in range(n + 1)])({i: v for i, v in enumerate(pascal_line(n - 1))})
pascal_triangle = lambda n: [pascal_line(x) for x in range(n)]
sierpinski      = lambda n: '\n'.join([''.join(['X' if odd(v) else ' ' for v in l]) for l in pascal_triangle(n)])

if __name__ == '__main__':
    print(sierpinski(2 ** 6))