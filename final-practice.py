#Final Practice

##1 Leaf Year function

def leaf():
    year = int(input("년도를 입력하세요: "))
    if year > 3000 or year <1:
        print("1~3000사이의 정수를 입력해주세요.")
    elif year%400 == 0 or (year%4 == 0 and year%100 != 0):
        print("윤년입니다.")
    else: 
        print("평년입니다.")

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
    seq = [ ]
    for i in range(1,n+1):
        seq.append(fibonacci_r(i))
    return seq

##4 fibonacci sequence(with memoization)

def fibonacci_m():
    n = int(input("출력할 피보나치 수열의 항의 개수를 입력해주세요: "))
    seq = [1, 1]
    if n == 1 or n == 2:
        return 1
    for i in range(2,n):
        seq.append(seq[i-1]+seq[i-2])
    return seq

##5 fibonacci sequence(with binet's formula)

def fibonacci_binet():
    n = int(input("출력할 피보나치 수열의 항의 개수를 입력해주세요: "))
    seq = []
    phi = (1+5**0.5)/2
    for i in range(1,n+1):
        num = int(((phi)**i - (1-phi)**i)/(5**0.5))
        seq.append(num)
    return seq


leaf()
