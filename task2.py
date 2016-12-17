def getFibonacciNum(n: int) -> int:
    if n < 3:
        return 1
    return getFibonacciNum(n - 1) + getFibonacciNum(n - 2)
