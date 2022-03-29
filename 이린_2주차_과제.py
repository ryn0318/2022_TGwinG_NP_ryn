# 문제 1번
def sum(a,b):
    return a+b

# 문제 2번
def sub(a,b):
    return a-b

# 문제 3번
def mul(a,b):
    return a*b

# 문제 4번
def div(a,b):
    return a/b

# 문제 5번
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

# 문제 6번
def short():
    lylic = "life is short art is long"
    return lylic[8:13]

print(short())

# 문제 7번
def myReverse(string):
    return (string[::-1])

print(myReverse('hello'))



# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오 : ")
    hobby = input("취미를 입력하시오 : ")
    univ = input("재학 중인 대학을 입력하시오 : ")
    birth = input("생년월일을 입력하시오 (예시:981128) : ")
    intro = "제 이름은 {이름}입니다. 제 취미는 {취미}이구요. 저는 {재학_중인_대학}를 다니고 있습니다. 제 생일은 {월}월 {일}일 입니다.".format(이름=name, 취미=hobby,재학_중인_대학=univ,월=birth[2:4],일=birth[4:])
    return intro

print(letMeIntroduceMyself())

# 문제 9번
def calcAI():
    num1 = float(input("첫번째 숫자를 입력하시오 : "))
    num2 = float(input("두번째 숫자를 입력하시오 : "))
    sum = num1 + num2
    return print("두 수의 합은",sum,"입니다.")

print(calcAI())



