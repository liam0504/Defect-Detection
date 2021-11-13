import numpy as np #支援矩陣運算
import os,csv
import matplotlib.pyplot as plt
import pandas as pd
from keras import optimizers
from keras.applications import VGG16
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
from keras_applications.densenet import models
from keras_preprocessing.image import ImageDataGenerator

train_path = 'train_images/train/'
valid_path = 'train_images/valid/'
test_path = 'train_images/test/'
###正規化~~~
train_datagen = ImageDataGenerator(rescale=1./255 )
train_generator = train_datagen.flow_from_directory(
      train_path,
      target_size=(256, 256),
      batch_size=32,
      class_mode='categorical')
valid_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = valid_datagen.flow_from_directory(
        valid_path,
        target_size=(256, 256),
        batch_size=32,
        class_mode='categorical')
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
        test_path,
        target_size=(256, 256),
        batch_size=32,
        class_mode='categorical')

conv_base = VGG16(weights='imagenet', include_top=False,input_shape=(256,256,3))
model=Sequential() # 建立模型
model.add(conv_base)
#根據PPT所做的階層
model.add(Conv2D(filters=32,kernel_size=(2,2),padding='same',input_shape=(256,256,2),activation='relu')) # 建立卷基層
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(1,1)))

model.add(Conv2D(filters=64,kernel_size=(2,2),padding='same',activation='relu'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=128,kernel_size=(2,2),padding='same',activation='relu'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=256,kernel_size=(2,2),padding='same',activation='relu'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(32))
model.add(Dense(64))
model.add(Dense(6,activation='softmax'))

model.compile(loss="categorical_crossentropy", optimizer=optimizers.RMSprop(lr=0.00002), metrics=['accuracy']) #損失函數、優化方法、成效衡量
history = model.fit_generator(
      train_generator,
      steps_per_epoch=train_generator.samples//train_generator.batch_size,
      epochs=50,
      validation_data=validation_generator,
      validation_steps=validation_generator.samples//validation_generator.batch_size
)
def show_train(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.xlabel('Epoch')
    plt.ylabel(train)
    plt.legend(['train','validation'],loc='upper left')
    plt.show()
show_train(history,'accuracy','val_accuracy')
show_train(history,'loss','val_loss')

test_loss, test_acc = model.evaluate_generator(
	test_generator,
	steps=test_generator.samples//test_generator.batch_size)

print('test acc:', test_acc)
print('test lost:', test_loss)
model.save('matlab_final_model.h5')
