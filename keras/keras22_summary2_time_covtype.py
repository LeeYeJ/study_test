#분류
#캐글, 따릉이, 디아벳 최대 업로드수 해서 등수까지 스냅샷 찍어서 금요일 주말 내내 제출
from sklearn.datasets import fetch_covtype
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.python.keras.callbacks import EarlyStopping
import numpy as np
import pandas as pd

datasets=fetch_covtype() # 인터넷에서 가져와서 내 로컬에 저장되는거임. 만약 엉키면(에러) 파일 경로 찾아서 직접 삭제해줘야됨 / 사이킷럭 삭제시 cmd 창에 uninstall
x=datasets.data
y=datasets['target']

print(x.shape,y.shape) # (581012, 54) (581012,)
print(np.unique(y))  # [1 2 3 4 5 6 7] # 1부터 시자하는데 원핫인코딩(판다스,사이킷런,케라스)할때의 차이를 보고 사용 
print(datasets.DESCR)

# # 원핫인코딩
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
y= y.reshape(-1,1)
y=encoder.fit_transform(y).toarray()
#데이터 분리
x_train,x_test,y_train,y_test=train_test_split(
    x,y, shuffle=True, random_state=2000,train_size=0.9
)

model=Sequential()
model.add(Dense(2,input_dim=54))
model.add(Dense(87,activation='relu'))
model.add(Dense(3,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(7,activation='softmax'))

model.summary() # 터져버렸음 껐다 다시 켜기
'''
________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 23)                1265
_________________________________________________________________
dense_1 (Dense)              (None, 23)                552
_________________________________________________________________
dense_2 (Dense)              (None, 32)                768
_________________________________________________________________
dense_3 (Dense)              (None, 23)                759
_________________________________________________________________
dense_4 (Dense)              (None, 43)                1032
_________________________________________________________________
dense_5 (Dense)              (None, 7)                 308
=================================================================
Total params: 4,684
Trainable params: 4,684
Non-trainable params: 0
'''
#컴파일 훈련
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['acc'])
es=EarlyStopping(monitor='val_acc',mode='auto',patience=50)
#시간측정
import time
start_time=time.time() #현시간 반환

model.fit(x_train,y_train,epochs=5,batch_size=10000,validation_split=0.1,callbacks=[es])

end_time=time.time()

results=model.evaluate(x_test,y_test)
print('results :', results)

print('걸린 시간은 :', round(end_time-start_time,2)) #python 자체 예약어 ->round , ,2는 소수 둘째자리까지

y_pre= model.predict(x_test)

y_test_acc=np.argmax(y_test, axis=1) 
print(y_test_acc) 
y_pre=np.argmax(y_pre,axis=1)
print(y_pre) 

acc=accuracy_score(y_pre,y_test_acc)   
print('acc :', acc)

'''
Epoch 450/5000
95/95 [==============================] - 0s 4ms/step - loss: 0.5608 - acc: 0.7653 - val_loss: 0.5759 - val_acc: 0.7528
1816/1816 [==============================] - 1s 634us/step - loss: 0.5734 - acc: 0.7569
results : [0.5733653903007507, 0.7568758130073547]
[1 0 0 ... 0 1 1]
[1 0 0 ... 0 1 1]
acc : 0.7568758390416853
'''

'''
x_train,x_test,y_train,y_test=train_test_split(
    x,y, shuffle=True, random_state=2000,train_size=0.9
)

471/471 [==============================] - 1s 2ms/step - loss: 0.5011 - acc: 0.7910 - val_loss: 0.5064 - val_acc: 0.7902
Epoch 545/5000
471/471 [==============================] - 1s 2ms/step - loss: 0.5006 - acc: 0.7908 - val_loss: 0.4991 - val_acc: 0.7935
1816/1816 [==============================] - 1s 663us/step - loss: 0.5034 - acc: 0.7914
results : [0.5034043192863464, 0.7914013266563416]
[0 0 0 ... 1 1 1]
[0 0 0 ... 1 1 0]
acc : 0.7914013286978073

'''
#배치가 크면 터져 왜? 연산횟수의 문제가 아니고 한번에 많은 메모리를 잡아먹으니까