#Final Practice

##1 사용자의 입력(1~3000 사이의 정수)년도 가 윤년인지 알려주는 function


##2 ethiopian multiplication


##3 fibonacci sequence(recursion)


##4 fibonacci sequence(with memoization)



##5 fibonacci sequence(with binet's formula)

def fibonacci_binet():
    n = int(input("출력할 피보나치 수열의 항의 개수를 입력해주세요: "))
    seq = []
    phi = (1+5**0.5)/2
    for i in range(1,n+1):
        num = int(((phi)**i - (1-phi)**i)/(5**0.5))
        seq.append(num)
    return seq

