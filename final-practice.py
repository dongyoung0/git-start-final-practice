#Final Practice

##1 사용자의 입력(1~3000 사이의 정수)년도 가 윤년인지 알려주는 function


##2 ethiopian multiplication


##3 fibonacci sequence(recursion)


##4 fibonacci sequence(with memoization)

def fibonacci_m():
    n = int(input("출력할 피보나치 수열의 항의 개수를 입력해주세요: ")
    seq = [1,1]
    if n == 1 or n == 2:
        return 1
    for i in range(2,n):
        seq.append(seq[i-1]+seq[i-2])
    return seq

##5 fibonacci sequence(with binet's formula)



