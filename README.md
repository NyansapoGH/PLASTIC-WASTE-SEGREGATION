# PLASTIC-WASTE-SEGREGATION

## Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Procedure](#procedure)
  * [Datasets](#datasets)
  * [Model](#model)
  * [Installation](#installation)
  * [Plastic Waste Prediction](#waste_prediction)
  

## Overview
This is a PLASTIC-WASTE-SEGREGATION Web Application built using both Streamlit and PyTorch.

## Motivation
The present way of separating waste/garbage is the hand-picking method, whereby someone is
employed to separate out the different objects/materials. 
The person, who separate waste, is prone to diseases due to the harmful substances in the garbage. 
I recently payed a visit to a colleague of mine at the Recycling Plant (KNUST) and the present way of separating plastic waste is by hand-picking, whereby they manually separate the waste into the various types.
In so doing, they're prone to health problems and also production is not at its best 
This gave me the idea to develop an automated system which will be faster and more accurate to sort the plastic waste than the manual ways. 



For people who are not experts at Django or Flask, Streamlit can be a good alternative to build custom Python web apps for data science.
I chose image classification as the task here because computer vision is one of the most popular areas of AI currently, powered by the advancement of deep learning algorithms.

## Procedure
  * Install Streamlit
  * Build UI for the Streamlit web app
  * Build Model 
  * Test Results using the web app
  * Next Steps
  

## Datasets
For the experiment with deep neural networks, it is important to gather a lot of data for each labelled class.The images in the dataset was obtained from (Plastic Waste DataBase of Images – WaDaBa) in which there are 4000  images and have been divided into groups based on the type of materials which are commonly  known  as  Resin  Identification  Code  (RIC). The seven  RIC symbols are  PET,  HDPE,  PVC,  LDPE,  PP,  PS, and Other. 

* Link to the Datasets  http://wadaba.pcz.pl/
  ## Reference for datasets
 * Bobulski J., Piatkowski J., PET waste classification method and Plastic Waste DataBase WaDaBa, Conference Proc. IP&C 2018, Advances in Intelligent Systems and          Computing, vol. 681, Springer Verlag, 2018, pp.57-64.PDF

* Bobulski J., Kubanek M., Deep Learning for Plastic Waste Classification System, Applied Computational Intelligence and Soft Computing, 2021, art. no. 6626948 DOI:      10.1155/2021/6626948 PDF>


## Model
I have chosen the pretrained ResNet50 model to perform classification. 
To figure out how the model was built, take a look at the jupyter notebook entitled `Plastic Waste Model.ipynb`...(You will find it very self-explanatory)
I Used Google Colab to build and train the Model . So depending on the platform you prefer, you have to research about how to use it.


  
## Installation
```bash
pip install -r requirements.txt
```
then, you run the jupyter file `Plastic Waste Model.ipynb`  to  build and train the Model 

then finally, you run the code by typing the command below in your terminal to test the streamlit web app
```bash
streamlit run app.py
```

## Plastic Waste Prediction
The Results from the training of the Model.
The Training Accuracies and Losses Against Number of EPOCHS Run.
With the Achievements of 98% Accuracy

* Epoch 1: train_loss: 1.1269, val_loss: 0.9976, val_acc: 0.9336
* Epoch 2: train_loss: 0.9527, val_loss: 0.9671, val_acc: 0.9570
* Epoch 3: train_loss: 0.9269, val_loss: 0.9235, val_acc: 0.9883
* Epoch 4: train_loss: 0.9194, val_loss: 0.9134, val_acc: 1.0000
* Epoch 5: train_loss: 0.9135, val_loss: 0.9208, val_acc: 0.9883
* Epoch 6: train_loss: 0.9116, val_loss: 0.9157, val_acc: 0.9961
* Epoch 7: train_loss: 0.9122, val_loss: 0.9223, val_acc: 0.9609
* Epoch 8: train_loss: 0.9095, val_loss: 0.9238, val_acc: 0.9922
* Epoch 9: train_loss: 0.9133, val_loss: 0.9141, val_acc: 1.0000
* Epoch 10: train_loss: 0.9117, val_loss: 0.9089, val_acc: 1.0000


screenshots from testing with the streamlit web app 
<!--- Add image --->
* ![Study for Finals](https://github.com/NyansapoGH/PLASTIC-WASTE-SEGREGATION/blob/95269f0519d54a6d0fa8913c7361ce5713d5d72b/Streamlit/Screenshots/pic%203.png?raw=true)
* ![Study for Finals](https://github.com/NyansapoGH/PLASTIC-WASTE-SEGREGATION/blob/95269f0519d54a6d0fa8913c7361ce5713d5d72b/Streamlit/Screenshots/selected%202.png?raw=true)
* ![Study for Finals](https://github.com/NyansapoGH/PLASTIC-WASTE-SEGREGATION/blob/95269f0519d54a6d0fa8913c7361ce5713d5d72b/Streamlit/Screenshots/pic%201.png?raw=true)



