import numpy as np
from keras.preprocessing import image
import tensorflow as tf
import os
from tensorflow import keras
model = keras.models.load_model("index/static/model.h5")


def checkIfItsCovid():
    print(os.listdir('index/static/upload/upload')[0])
    img=image.load_img('index/static/upload/upload/'+os.listdir('index/static/upload/upload')[0],target_size=(160,160))
    img=image.img_to_array(img)
    img=np.array(img,dtype="float32")
    img=np.expand_dims(img, axis= 0)
    y_pred=model.predict(img)
    predictions = tf.nn.sigmoid(y_pred)
    dir = 'index/static/upload/upload'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    print("Prediction = ")
    print( predictions)
    #4.839611847273773e-06
    # 
    # tf.Tensor([[4.839612e-06]], shape=(1, 1), dtype=float32)
    # tf.Tensor([[4.839612e-06]], shape=(1, 1), dtype=float32)
    if float(predictions[0])>0.5:
        return 'is a dog'
    else:
        return 'is a cat'
    
    # check_dataset = image.ImageDataGenerator(
    #     rescale=1./255
    # )
    # check_generator = check_dataset.flow_from_directory(
    #     'index/static/upload',
    #     batch_size = 32,
    #     class_mode = 'binary'
    # )

    # # j = np.array(X-test)
    # result = model.predict(check_generator)[0][0]
    # print(result)
    # dir = 'index/static/upload/upload'
    # for f in os.listdir(dir):
    #     os.remove(os.path.join(dir, f))

    # if (result > 0.5):
    #     return 'is a cat'
    # else:
    #     return 'is a dog'