# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점

def calcCircleArea(r):
    result = float()
    
    import math
    a=math.pow(r,2)
    b=math.pi
    c=a*b
    result=round(c,2)
    return result

def calcLog(a, b):
    result = float()
    
    import math
    result = round(math.log(a,b),2)
    return result

def calcSin(x):
    result = float()
    
    import math
    result=round(math.sin(x),2)
    return result

def calcFactorial(x):
    result = float()
    
    import math
    result=round(math.factorial(x),2)
    return result

def calcCombination(n, r):
    result = int() 
    
    import math
    result=math.comb(n,r)
    return result
    
def calculator(order):
    answer = 0
    
    if order == calcCircleArea :
        calcCircleArea()
    elif order == calcLog:
            calcLog()
    elif order == calSin :
            calSin()
    elif order == calcFactorial:
            calcFactorial()
    elif order == calcCombination:
            calcCombination()

    return answer