# 정확률 =  9.4266280

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dropout,Dense,Rescaling
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.densenet import DenseNet121
from tensorflow.keras.utils import image_dataset_from_directory
import pathlib
import pickle
import matplotlib.pyplot as plt

data_path=pathlib.Path("datasets/stanford_dogs/images/images")

# 폴더에서 데이터 읽기
train_ds=image_dataset_from_directory(data_path,validation_split=0.2,subset='training',seed=123,image_size=(224,224),batch_size=16)
test_ds=image_dataset_from_directory(data_path,validation_split=0.2,subset='validation',seed=123,image_size=(224,224),batch_size=16)

# DenseNet121을 백본으로 사용 weights는 imageNet으로 사전 학습된 가중치 로드, 모델의 뒤쪽에 있는 완전 연결층 제외, 신경망 입력 텐서 크기 지정
base_model=DenseNet121(weights='imagenet',include_top=False,input_shape=(224,224,3))
cnn=Sequential()
# 입력 텐서를 [0,1]로 정규화
cnn.add(Rescaling(1.0/255.0))
cnn.add(base_model)
# 백본 출력텐서를 1차원으로 flattening
cnn.add(Flatten())
cnn.add(Dense(1024,activation='relu'))
cnn.add(Dropout(0.75))
# 결과 출력을 위한 완전연결층, 120개 부류, softmax
cnn.add(Dense(units=120,activation='softmax'))

# learning rate는 미세조정 방식의 전이학습, 학습률을 아주 작게 설정하여 특징 추출을 담당하는 층의 가중치를 유지
# epochs 미세 조정을 위해 epoch의 수를 늘려 오래 학습
cnn.compile(loss="sparse_categorical_crossentropy", optimizer=Adam(learning_rate=0.000001), metrics=['accuracy'])
hist=cnn.fit(train_ds,epochs=2, validation_data=test_ds,verbose=1)

print("정확률 = ", cnn.evaluate(test_ds,verbose=0)[1]*100)

# 미세 조정된 모델을 파일에 저장
# 비전 에이전트 7을 위해 모델을 저장
cnn.save('cnn_for_stanford_dogs.h5')


f=open('dog_species_names.txt','wb')
pickle.dump(train_ds.class_names,f)
f.close()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Accuracy graph')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'])
plt.grid()
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss graph')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'])
plt.grid()
plt.show()
