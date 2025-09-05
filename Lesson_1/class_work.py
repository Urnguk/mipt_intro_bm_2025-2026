# def func(x):
#     if x > 3:
#         return
#     print(x)
#     func(x + 1)
#     print(x)
#
#
# func(0)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_din(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


def fib_memo(n, memo=None):
    if memo is None:
        memo = [0, 1]
    if n >= len(memo):
        memo.append(fib_memo(n - 1, memo) + fib_memo(n - 2, memo))
    return memo[n]


print(fib_memo(500))
print(fib(5), fib_din(5))