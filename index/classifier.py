import numpy as np
from keras.preprocessing import image
import tensorflow as tf
import os
from tensorflow import keras
model = keras.models.load_model("index/static/model.h5")


def checkIfItsDogOrCat():
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
    
    if float(predictions[0])>0.5:
        return 'is a dog'
    else:
        return 'is a cat'
    
  