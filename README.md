# Vehicle Classifier App:
![Python 3.6](https://img.shields.io/badge/Python-v3.6-green) ![keras](https://img.shields.io/badge/keras-v2.2-yellow)  ![tensorflow](https://img.shields.io/badge/tensorflow-v2.2-red) ![numpy](https://img.shields.io/badge/numpy-1.20-blue) ![flask](https://img.shields.io/badge/flask-v-yellowgreen)



Table of contents
=================

<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Problem Statement](#Problem-Statement)
   * [Abstract](#Abstract)
   * [DEMO](#DEMO)
   * [Data Gathering/Preprocessing](#Data-Gathering)
   * [Model Training](#Model-Training)
      * [How to Train](#Model-Training)
      * [Observations](#Observations)
   * [Complete Setup](#Complete-setup)
      * [Dependency](#Dependency)
      * [How to Run](#How-To-Run)
   * [Bug/Feature Request](#Bug/Feature-request)
   * [Technologies Used](#Technologies-used)
<!--te-->


## Problem Statement
Raw Dataset in .pdf file format extension is given which consists of images of different vehicles. Using this dataset you need to prepare an Machine learning model which classifies vehicles in categories based on its body types i.e size such as Sedan, Hatchback, SUV, MUV etc. 



## Abstract
```bash
Intelligent vehicle detection and classification are becoming increasingly important in the field of highway management.
However due to the different sizes of vehicles, their detection remains a challenge that directly affects the accuracy 
of vehicle classification. The proposed solution encounters the problem statement and classifies the vehicle on basis of
its body type. Transfer learning approach with pretrained weights of Resnet50 classification model is used for the problem
statement.
```

## DEMO




## Data Gathering/Preprocessing
We have different images of vehicles in form of a pdf document. [Click here!](https://drive.google.com/drive/folders/1QjfB6QME1mEPmvsSvPvoNTHqDiLbPdsO?usp=sharing) for downloading dataset.
Due to very less amount of dataset which could suffer our model from bad accuracy. Data Augmentation has been performed, Taking 10-15 Augmented images per image sample.
This helped in getting more amount of vehicle images, so that model has lot of data to learn and train itself for providing better results.

```bash
Refer the below file for the keras Data Augmentation code which is used for our problem statement use case.
```
[Vehicle Data Augmentation Keras Code](https://colab.research.google.com/drive/1qvjhMG-NnaB_NRdsIqKIXCErJ95Q_F1i?usp=sharing)

## Model Training
Once pure data is collected by doing various feature engineering techniques. we have to feed this data to ML Model which is resnet50 in this case.
Find below the Google colab link for performing model training.

1. __How To Train__: Refer the provided Google colab shared file here ( [Model Training Colab File](https://colab.research.google.com/drive/1etWCOXAN__oe-YDwzm1ZinCymCMx4y8b?usp=sharing)). With respect to the dependencies for model training, please prefer using Tensorflow v2.2 for better compatiblity. All the steps regards the "How to Train" our resnet50 model are mentioned inside the Google Colab ModelTraining file itself.

```bash
Some observations during the model training, Parameter versus the description is mentioned in below tabular form.
```

| Parameter | Description |
| --- | --- |
| `Tensorflow` | version 2.2 |
| `Pre-Trained model` |  **Resnet50** |
| `Data Augmentor` | Keras |
| `Image Size`     | 224, 224 |
| `Batch Size` | 32 |
| `Loss Function` |  Categorical_cross_entropy |
| `Optimizer` | Adam |
| `Epochs` |  **200** |
| `Loss` | **0.1058** |
| `Accuracy` | **0.9577** |
| `Val Loss` | **0.8386** |
| `Val Accuracy` | **0.8390** |


3. __Graphical Intuition__: 


__Train Vs Test Loss__

![loss metric](https://user-images.githubusercontent.com/63975688/124378785-ee0bef80-dcd0-11eb-8eb2-98dbf4557e9e.PNG)


__Train Vs Test Accuracy__

![Accuracy metric](https://user-images.githubusercontent.com/63975688/124378781-e8aea500-dcd0-11eb-9480-8868f57a9261.PNG)



## Complete Setup
The VechicleClassifierApp is coded in python version 3.6, with other libraries as Tensorflow, Keras, opencv-python, numpy etc. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). Upgrade using pip package if you are using any lower version. 

## * Inference
```bash
* All the images from the pdf documents are extracted and are placed to the respective class folders to which it belong to.
  for eg. sedan class name folder is created and all images comprises to sedan cars are placed inside that folder.
* splitting of dataset into two parts, Training and Validation.
* Pre-Trained weights of resnet50 model are taken as model training on top of Vehicle dataset we extracted from pdf files.
* Once the complete dataset is trained on Google Colab, model is saved as .h5 extension to the local.
* During the image prediction, Image file is uploaded and read using cv2 and data preprocessing is done before predicting.
* Softmax function converts the image into some probability value between 0 to 1. where the max probability represents higher
  chances of value being TRUE.
* As we have taken 5 classes over here, so softmax returns a vector of 5 different probablity values.
* Using Argmax(), out of all values maximum probability is fetched.
* To the class this maximum probabilty belong to, predictor valids True for that class.
* Hence, This prediction is reflected to the Web UI.
```



1. __Dependency__:

The dependencies are mentioned in the requirements.txt file. Go with the below mentioned command for installing them in one go.
```bash
pip install -r requirements.txt
```



2. __How To Run__:
Once you have installed all the dependencies using the above command. Follow the below steps:

* Flask Api is used for end to end VehicleClassifierApp development.
* Clone the VehicleClassifierApp repo, Unzip it and open in any IDE (Pycharm is recommended).
* Create a virtual environment for python v3.6.
* Install all requirements by using above mentioned command.
* After installing all the dependencies, run main.py file.
* main.py file will open a default page on local server.
* Upload the file (Image) belonging to the class (Hatchback, SUV, MUV, Sedan, Other) and click on predict.
* Prediction successfull.

## Bug / Feature Request

If you find some bug/defect or if you'd like to request a new function, feel free to do so by opening an issue ![here](https://github.com/RajeshKGangwar/VehicleClassifierApp/issues/new).

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank"></a> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-ar21.svg" alt="open-cv" width="150" height="150"/>
  <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-ar21.svg" alt="open-cv" width="150" height="150"/>
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg" alt="open-cv" width="150" height="150"/>
  <img src="https://www.vectorlogo.zone/logos/python/python-ar21.svg" alt="open-cv" width="150" height="150"/> <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="numpy" width="150" height="150"/>

