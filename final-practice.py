#Final Practice

##1 사용자의 입력(1~3000 사이의 정수)년도 가 윤년인지 알려주는 function

def leaf_year():
    year = int(input("년도를 입력하세요: "))
    if year > 3000 or year <1:
        print("1~3000사이의 정수를 입력해주세요.")
    elif year%400==0 or (year%4==0 and year%100!=0):
        print("윤년입니다")
    else: 
        print("평년입니다")

##2 ethiopian multiplication


##3 fibonacci sequence(recursion)


##4 fibonacci sequence(with memoization)



##5 fibonacci sequence(with binet's formula)



