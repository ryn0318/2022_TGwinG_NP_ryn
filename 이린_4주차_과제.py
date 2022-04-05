# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번
def intervention(queue):
    answer = list()
    
    if "성은" in queue :
        if "성은" in queue[0:5]:
            queue.append("승호")
        else :
            i = queue.index("성은")
            queue.insert(i+1,"승호")
    else :
        queue.append("승호")

    answer=queue
    return answer

# 문제 2번
def pascal(n):
    answer = list()
    # your code
    return answer

# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()

    new_searchWords = [i for i in searchWords if entry in i]
    new_searchWords.sort()
  
    answer = new_searchWords
    return answer


# 문제 4번
def stock_price(stockChart):
    answer = str()
    
    check = False
    sum = 0
    min = 0

    for i in range(len(stockChart)) :
        if stockChart[i]>0 :
            check = True
        
        sum += stockChart[i]
    
        if sum<min:
            min = sum
            a = i
        
    if check == True :
        return str(len(stockChart)-a-1)+"일 전에 샀어야지 으이구"
    else :
        return "아니야 조금만 더 기다려"

# 문제 5번
def decryption(letter):
    answer = str()
    # your code
    return answer