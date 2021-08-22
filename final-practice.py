#Final Practice

##1 사용자의 입력(1~3000 사이의 정수)년도 가 윤년인지 알려주는 function


##2 ethiopian multiplication


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


##4 fibonacci sequence(with memoization)




##5 fibonacci sequence(with binet's formula)



