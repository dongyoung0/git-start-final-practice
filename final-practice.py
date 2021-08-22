#Final Practice

##1 Leaf Year function

##2 Ethiopian multiplication

def eth_mult():
    a = int(input("첫번째 수를 입력해주세요: "))
    b = int(input("두번째 수를 입력해주세요: "))
    result = 0
    while a>0:
        if a%2 == 1:
            result += b
        a //= 2
        b *= 2
    return result

##3 fibonacci sequence(recursion)

def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)

def fibonacci_recursion():
    n = int(input("출력할 피보나치 수열의 항의 개수를 입력해주세요: "))
    seq = []
    for i in range(1,n+1):
        seq.append(fibonacci_r(i))
    return seq


##4 fibonacci sequence(with memoization)


##5 Fibonacci sequence(with binet's formula)


