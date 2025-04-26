## Convolutional Neural Network for Traffic Sign Recognition

### Introduction

This is a Traffic Sign Recognition model using CNN (Convolutional Neural Network). Traffic sign recognition has a wide range of applications in our real world such as driver assistance and safety(ADAS), urban scene understanding, automated driving, or even sign monitoring for maintenance. It is a relatively constrained problem in the sense that signs are unique, rigid and intended to be clearly visible for drivers, and have little variability in appearance. Drivers missed traffic signs because different obstacles or lack of attentiveness or the high speed of vehicles happens in most of time. Automating the process of classification of the traffic signs would help reducing accidents. The dataset provided by the GTSRB competition presents a wide range of difficult challenges due to real-world variabilities such as viewpoint variations, lighting conditions (saturations, low-contrast), motion-blur, occlusions, sun glare, physical damage, colors fading, graffiti, stickers and an input resolution as low as 15x15. 

In this project, I am using TensorFlow as a ML framework and a couple of dependencies like numpy , matplotlib  and scikit-image . Here I present results on the German traffic sign recognition benchmark, a 43 class, single-image classification challenge. I first give a brief description of our dataset, then describe the data preprocessing, the CNN model I built,and training process. Finally, I visualize the result and present experimental results.

### Dataset
[The German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset)

