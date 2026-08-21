memo = {}

def f(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = f(n - 1) + f(n - 2)
    return memo[n]

print(f(6))  
