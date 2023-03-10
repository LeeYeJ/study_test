# x는 2개 y는 1개

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#1. 데이터
x = np.array( #행무시, 열우선
    [
        [1,1], # 1,1일때 11
        [2,1], # 2,1일때 12...
        [3,1],
        [4,1],
        [5,2],
        [6,1.3],
        [7,1.4],
        [8,1.5],
        [9,1.6],
        [10, 1.4]
    ]   
)
y = np.array([11,12,13,14,15,16,17,18,19,20])

print(x.shape) #(10, 2) 2개의 특성을 가진 10개의 데이터
print(y.shape) #(10,)

#2. 모델구성
model=Sequential()
model.add(Dense(3,input_dim =2)) # x 열의 갯수와 동일해야한다. ,즉 특성의 갯수
model.add(Dense(7))
model.add(Dense(5))
model.add(Dense(5))
model.add(Dense(5))
model.add(Dense(1))

#3.컴파일 훈련
model.compile(loss='mae', optimizer='adam')
model.fit(x,y,epochs=1000,batch_size=2)

#4 평가 예측
loss = model.evaluate(x,y) # 위에 가중치에 데이터를 넣어서 무슨 값이 나오는지 평가한다. (나중에는 데이터 안넣음 왜냐 훈련되지않은 데이터를 평가하기 위해) 즉, 모델의 정확도를 평가힐 수 있다
print('loss :', loss) #fit에서 생성된 w값을 가지고  평가를 하는 것이다.

result = model.predict([[10,1.4]]) #[10,1.4]을 넣아주면 벡터형태라 오류뜬다 (10,) 따라서 [[10,1.4]]로 변경
print('[10,1.4]의 값은 : ', result)


#loss : 0.019304942339658737
#1/1 [==============================] - 0s 72ms/step
#[10,1.4]의 값은 :  [[20.007746]]



