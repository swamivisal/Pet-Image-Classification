######################################IMPORTING ESSENTIAL LIBRARIES######################################
import numpy as np 												
import cv2 												
import os 													
import random 												
##########################################DATASET PREPARATION##########################################
directory = "PetImages"											
animals = ["Cat","Dog"] 											
training_data = [] 												
for animal in animals: 											
	path = directory+"/"+animal 										
	index = animals.index(animal) 										
	for img in os.listdir(path): 										
		try:											
			img_array = cv2.imread(path+"/"+img,0)							
			new_array = cv2.resize(img_array, (50,50)) 						
			training_data.append([new_array,index]) 							
		except: 											
			pass 										
random.shuffle(training_data) 											
data = training_data[:10]											
for features,labels in data: 											
	print(labels) 											
np.save("Datasets/TRAIN.npy",training_data) 									
#########################################################################################################
