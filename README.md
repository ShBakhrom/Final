# Dogs vs Cats

Authors: Vinith Babu Muruganantham, Tharoon Veerasethu, Bakhrom Shukrathov, Mohammed Najith

Final Project AIDI-2004

# Introduction:
There are a lot of images on google. Just a small search on google for the images, could show that there are a lot of images. How do you classify these images and how to do it effectively? There are alot of things that go into consideration when it comes to this. In just a class we have 1000 of images and there are 1000s of classes that are present. Can we classify all of them manually. There are many new images being added to these classes. It is time consuming and it is hard to do. This is where AI comes to play. All we have to do is to train it and it should do the work. But the hardest part in AI is not model building, it's the deploying of the model so that it can be scaled. 
Though there are various ways to do it, in this report we will be looking at how we tackled the problem of classifying just cat and dog images, how we leveraged the model using transfer learning and how we deployed the model for public use of the model.

# Collecting and Understanding the Data:
The data was taken from Kaggle, where there are 25,000 images of cats and dogs (https://www.kaggle.com/c/dogs-vs-cats/data). The data does not have any metadata giving the class type for each image. They have two zip files containing the data, which are train and test. According to Kaggle, the train data is for training the model and test data is for testing the model for its performance. But since the dataset is large, we only used the train zip to train the model and the test zip was ignored. The dataset was downloaded using the Kaggle API token. The dataset was directly downloaded to my drive.

# Build Model
There are a lot of models that were tried. As the dataset was huge, it was a huge issue to select the right model as there is not enough computational power to handle the training. But in the end based on the performance transfer learning was adopted and Mobilenet v2 was used as the baseline model. The bottom of the model has an global average pooling layer, a dense layer, where the dense layer gives us the binary input. The loss function used for the model is binary cross entropy as there are only two classes that are being considered. The metrics that was chosen is accuracy, which is not a bad metric for a classification problem.

# Training the model:
The model was trained for 10 epoch. Though the model had a good accuracy in just 5 epoch, 10 was considered as the dataset was large (20,000 training images and 5000 test images). Fine tuning can be done on the model to improve the performance of the model. 


# UI:
UI was implemented using a Django framework. Django is an open-source framework that is based on Python language. The project consists of a simple UI which is represented as a form. Form contains 3 fields, first name, last name and picture of an animal All three fields have to be filled to proceed with classification. Once all inputs are entered and a POST request is received by the server, it saves the uploaded image at index/static/upload/upload. Design was implemented using simple css and fonts from the google fonts website. The fact that the framework is python based has helped a lot while integrating the trained model into the project. All we needed to do is create a separate file for classification called “classifier.py”  and import it in views.py. The classifier.py imports all required libraries for loading the saved .h5 model and running the classification process. Furthermore, it contains a special method called checkIfItsDogOrCat() which captures the uploaded image and runs classification on it

# Deployment
Deployment was the one of the most challenging parts of this assignment. Since we didn’t go with more methods learned in this class such as flask and heroku, we had to learn almost everything from the beginning. To be more specific, we decided to go with AWS (Amazon Web Services). There we have spinned up an Ubuntu virtual machine and cloned the Django project from the github repository. Created a virtual environment for installing all dependencies. Installed all required packages from the requirements.txt file. Next, we opened the port 8888 from the AWS dashboard and runned project on that port. 
