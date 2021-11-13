import numpy as np
from keras import models
from keras.preprocessing.image import ImageDataGenerator
import csv
final_test_path = "test_images"
model = models.load_model("matlab_final_model.h5")
final_test_datagen = ImageDataGenerator(rescale=1. / 255)
final_test_generator = final_test_datagen.flow_from_directory(
    final_test_path,
    target_size=(256, 256),
    class_mode='categorical',
    batch_size=1,
    shuffle=False)
predict = model.predict_generator(
    final_test_generator,
    steps=final_test_generator.samples // final_test_generator.batch_size)
with open('test.csv', newline='') as csvfile:
    name=[]
    rows = csv.DictReader(csvfile)
    for row in rows:
        name.append(row['ID'])
with open('test.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Label'])
    # print(len(predict))
    i = 0
    while i < len(predict):
        #image_name = final_test_generator.filenames[i]
        result = np.where(predict[i] == np.amax(predict[i]))[0][0]
        writer.writerow([name[i], result])
        i = i + 1
