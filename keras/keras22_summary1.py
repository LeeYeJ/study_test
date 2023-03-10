import numpy as np
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense

#데이터
x=np.array([1,2,3])
y=np.array([1,2,3])

#모델 구성
model = Sequential()
model.add(Dense(5,input_dim=1))
model.add(Dense(400000))
model.add(Dense(3000000))
model.add(Dense(2000000)) # 범
model.add(Dense(1))

model.summary() # 요약
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 5)                 10        # 바이어스까지 합해준것
_________________________________________________________________
dense_1 (Dense)              (None, 4)                 24
_________________________________________________________________
dense_2 (Dense)              (None, 3)                 15
_________________________________________________________________
dense_3 (Dense)              (None, 2)                 8
_________________________________________________________________
dense_4 (Dense)              (None, 1)                 3
=================================================================
Total params: 60
Trainable params: 60
Non-trainable params: 0
_________________________________________________________________
'''

