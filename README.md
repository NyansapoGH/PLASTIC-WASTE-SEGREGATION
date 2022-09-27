# PLASTIC-WASTE-SEGREGATION

## Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Procedure](#procedure)
  * [Model](#model)
  * [Installation](#installation)
  * [Garbage Prediction](#waste_prediction)
  

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
  
## Model
I have chosen the pretrained ResNet50 model to perform classification. 
To figure out how the model was built, take a look at the jupyter notebook entitled `ResNet50 Jupyter.ipynb`...(You will find it very self-explanatory)
I Used Google Colab to build and train the Model . So depending on the platform you prefer, you have to research about how to use it.


  
## Installation
```bash
pip install -r requirements.txt
```
then, you run the code by typing the command below in your terminal
```bash
streamlit run app.py
```


