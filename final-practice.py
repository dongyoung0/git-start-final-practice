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

##3 Fibonacci sequence(recursion)

##4 Fibonacci sequence(with memoization)

##5 Fibonacci sequence(with binet's formula)


