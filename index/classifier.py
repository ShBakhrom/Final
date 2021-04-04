import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image
from sklearn.metrics import classification_report, confusion_matrix
import os

TRAINING_PATH = 'index/static/newDataSet/train'
VALIDATION_PATH = 'index/static/newDataSet/validation'
TESTING_PATH = 'index/static/newDataSet/test'

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3),activation='relu',input_shape=(224, 224, 3)))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128,(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss=keras.losses.binary_crossentropy,optimizer='adam',metrics=['accuracy'])

#Training
training_dataset = image.ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
)

test_dataset = image.ImageDataGenerator(
    rescale=1./255
)

train_generator = training_dataset.flow_from_directory(
    TRAINING_PATH,
    target_size = [224, 224],
    batch_size = 32,
    class_mode = 'binary'
)
validation_generator = test_dataset.flow_from_directory(
    VALIDATION_PATH,
    target_size = [224, 224],
    batch_size = 32,
    class_mode = 'binary'
)
testing_generator = test_dataset.flow_from_directory(
    TESTING_PATH,
    target_size = [224, 224],
    batch_size = 32,
    class_mode = 'binary'
)

hist = model.fit(
    train_generator,
    steps_per_epoch=8,
    epochs = 10,
    validation_data = validation_generator,
    validation_steps = 2,
    verbose=0
)
results = model.evaluate(testing_generator)
print("test loss, test acc:", results)

def checkIfItsCovid():
    check_dataset = image.ImageDataGenerator(
        rescale=1./255
    )
    check_generator = check_dataset.flow_from_directory(
        'index/static/upload',
        target_size = [224, 224],
        batch_size = 32,
        class_mode = 'binary'
    )

    # j = np.array(X-test)
    result = model.predict(check_generator)[0][0]
    dir = 'index/static/upload/upload'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    if (result > 0.5):
        return 'has Covid-19'
    else:
        return 'does not Covid-19'