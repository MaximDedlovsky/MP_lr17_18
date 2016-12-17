def getFibonacciNum(n: int) -> int:
    if n < 3:
        return 1
    return getFibonacciNum(n - 1) + getFibonacciNum(n - 2)

n = int(input('Enter number: '))
print('n-th Fibonacci number: {0}'.format(getFibonacciNum(n)))
