# create model `test2` which has three function:阶乘函数：列表删值函数 等差数列求和函数

# create `factorial function` 阶乘函数
def f1(n):
    y = 1
    for i in range(1, n+1):
        y = y * i
    return y

# Create a function that delete list elements
def f2(lst, x):
    while x in lst:
        lst.remove(x)
    return lst

# Create a function that sums the arithmetic progressions
def f3(a, d, n):
    an = a
    s = 0
    for i in range(n-1):
        an = an + d
        s = s + an
    return s
