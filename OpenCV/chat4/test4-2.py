import numpy as np
import tensorflow as tf
import tensorflow.keras.datasets as ds

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# 데이터 준비
(x_train,y_train),(x_test,y_test) = ds.mnist.load_data()
x_train = x_train.reshape(60000,784)  # 1차원 구조로 변환
x_test = x_test.reshape(10000,784)
x_train = x_train.astype(np.float32)/255.0  # [0,1]로 정규화
x_test = x_test.astype(np.float32)/255.0
y_train = tf.keras.utils.to_categorical(y_train,10) # 원핫 코드로 변환
y_test = tf.keras.utils.to_categorical(y_test,10)

# 모델 선택(신경망 구조 설계)
mlp = Sequential()
# 은닉층 노드 개수 512, 출력층 노드 개수 10
# 은닉층 활성함수 tanh, 출력층 활성 함수 softmax
mlp.add(Dense(units=512,activation='tanh',input_shape=(784,)))
mlp.add(Dense(units=10,activation='softmax'))

# 학습
mlp.compile(loss="MSE", optimizer=SGD(learning_rate=0.01), metrics=['accuracy'])  #MSE 손실함수, SGD 옵티마이저, 학습률
mlp.fit(x_train,y_train,batch_size=128,epochs=50, validation_data=(x_test,y_test),verbose=2)  # 훈련 집합, 미니 배치 크기, 에폭 수

#예측 (성능 측정)
res=mlp.evaluate(x_test,y_test,verbose=0)
print("정확률 = ", res[1]*100)
