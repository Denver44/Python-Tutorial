# --------------------Recursive Approach ---------------------------
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


def fib(m):
    if m == 0:
        return 0
    else:

        return fib(m - 1) + m


print(fib(100))

# ----------------------- Iterative Approach-----------------------------------------------


def factorial(m):
    sum = 1
    for i in range(m):
        sum = sum * (i + 1)
    return sum


print(factorial(10))


def fib(m):
    sum = 0
    for i in range(m):
        sum = sum + i + 1
    return sum


print(fib(10))


# Note: Iterative approach is much faster than recursive approach. Both in time and space.
# But sometime we need recursive appracoh like in printing linnked list or binary tree.
