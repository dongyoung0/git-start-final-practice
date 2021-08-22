#Final Practice

##1 사용자의 입력(1~3000 사이의 정수)년도 가 윤년인지 알려주는 function


##2 ethiopian multiplication


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



##5 fibonacci sequence(with binet's formula)



