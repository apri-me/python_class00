
# TOP-Down   BOTTOM-UP

# Memory


def bu_fib(n):
    li = [0, 1]
    for i in range(2, n + 1):
        li.append(li[i - 1] + li[i - 2])
    return li[n]


def td_fib(n):
    li = [0] * (n + 1)
    return helper_func(n, li)


def helper_func(n, li):
    if n < 2:
        return n
    if li[n] != 0:
        return li[n]
    f = helper_func(n - 1, li) + helper_func(n - 2, li)
    li[n] = f
    return f


print(td_fib(100))
print(bu_fib(100))