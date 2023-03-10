import numpy as np

a=np.array([[1,2,3],[6,4,5],[7,9,2],[3,2,1],[2,3,1]])
print(a)
'''
[[1 2 3]
 [6 4 5]
 [7 9 2]
 [3 2 1]
 [2 3 1]]
'''
print(a.shape) #(5, 3)
print(np.argmax(a)) # 가장 높은 값의 위치값이 나온다. # 7
print(np.argmax(a, axis=0)) # 0은 행이다 (행끼리 비교한다 즉 세로로 각 행들을 비교)
#[2 2 1]
print(np.argmax(a, axis=1)) # 1은 열이다 (열끼리 비교한다 즉 가로로 각 열들을 비교)
#[2 0 1 0 1]
print(np.argmax(a, axis=-1)) 
#[2 0 1 0 1]
'''
가장 마지막 축, 현재 2차원이니까 가장 마지막축은 1
그래서 -1을 쓰면 이 데이터는 1과 동일
'''
