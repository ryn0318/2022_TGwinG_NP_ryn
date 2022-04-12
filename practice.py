#파스칼

# def pascal(n):
#     answer = list()
    
#     list1=[[1],[1,1]]
#     '''
#     list1[k][i+1] = list[k-1][i]+liskt[k][i+1] 
#     '''

#     for i in range(3,n+1):
#         list1.append([])
#         list1[i-1].append(1)
#         #list1[i-1][i-1]=1
#         for k in range(1,i-1):
#             list1[i-1].append(list1[i-2][k-1] + list1[i-2][k])
#         list1[i-1].append(1)
         
#     answer = list1
#     return answer[n-1]

# print(pascal(3))
# print(pascal(9))
# print(pascal(10))

# import math
# print(math.factorial(3))
# from math import factorial
# print(math.factorial(3))

# def calcCircleArea(r):
#     result = float()
    
#     import math
#     math.exp(r)
#     result=

#     return result



def calcSin(x):
    result = float()
    
    import math
    result=round(math.sin(x),2)
    return result
    
print(calcSin(60))