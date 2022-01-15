<div align='center'>
  
# 3D-Image-Classification
  
  </div>
3D CNN to Predict the presence of pneumonia from CT scans

## Introduction
This project will show the steps needed to build a 3D convolutional neural network (CNN) to predict the presence of viral pneumonia in computer tomography (CT) scans. 2D CNNs are commonly used to process RGB images (3 channels). A 3D CNN is simply the 3D equivalent: it takes as input a 3D volume or a sequence of 2D frames (e.g. slices in a CT scan), 3D CNNs are a powerful model for learning representations for volumetric data.

## Scope
Tumour is formed in human body by abnormal cell multiplication in the tissue. Early detection of tumors and classifying them to Benign and malignant tumours is important in order to prevent its further growth. MRI (Magnetic Resonance Imaging) is a medical imaging technique used by radiologists to study and analyse medical images. Doing critical analysis manually can create unnecessary delay and also the accuracy for the same will be very less due to human errors. The main objective of this project is to apply machine learning techniques to make systems capable enough to perform such critical analysis faster with higher accuracy and efficiency levels. The 3D Convolution Neural Network was implemented using Keras and TensorFlow.

## Data

+ **Brain with Tumour**
![alt text](https://github.com/mudit14224/3d-image-classification/blob/main/Images/cancer.png)

+ **Brain without Tumour**
![alt text](https://github.com/mudit14224/3d-image-classification/blob/main/Images/not%20cancer.png)

+ **A Montage of the Slices**
![alt text](https://github.com/mudit14224/3d-image-classification/blob/main/Images/3d.png)

## Frontend
### Home Page
![alt text](https://github.com/mudit14224/3d-image-classification/blob/main/Images/front1.PNG)
### Developers Page
![alt text](https://github.com/mudit14224/3d-image-classification/blob/main/Images/front2.PNG)
### Result
![alt text](https://github.com/mudit14224/3d-image-classification/blob/main/Images/front3.PNG)


## Tech Stack

+ Html
+ CSS
+ BootStrap
+ TensorFlow
+ Scipy
+ Nibabel
+ Flask
+ Numpy

## Running Instructions
Open the terminal and type the following 
```
$ git clone https://github.com/mudit14224/3d-image-classification
$ cd 3d-image-classification
$ python3 -m venv 3d-class-env
$ source 3d-class-env/bin/activate
$ pip3 install -r requirements.txt
$ python3 run.py
```

### Requirements

```
Werkzeug==1.0.1
matplotlib==3.4.0
Flask==1.1.2
tensorflow==2.5.0rc0
numpy==1.19.5
scipy==1.7.0
nibabel==3.2.1
```

## Developers

<table>
<tr align="center">


<td>

Mudit Jindal 

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/60563356?s=400&u=09a4f1f24803e0bd5cdc674e0fa021ca791fe126&v=4"  height="120"
alt="Mudit Jindal">
</p>
<p align="center">
<a href = "https://github.com/mudit14224" target="_blank"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/mudit-jindal-40521a18b/" target="_blank">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>






<td>

Mahima Khatri

<p align="center">
<img src = "https://avatars.githubusercontent.com/u/77387745?v=4"  height="120"
alt="Mahima Khatri">
</p>
<p align="center">
<a href = "https://github.com/MahimaKhatri" target="_blank"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/mahima-khatri-434a3b193/" target="_blank">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</tr>
</table>









