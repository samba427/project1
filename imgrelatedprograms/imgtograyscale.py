#try to convert an img to grayscale manually

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img=Image.open(r"C:\python_project1\project1\Luffy vs admirals.jpg")
print(img)
arr=np.array(img)

print(arr.shape)#the output is (a,b,3) where a is height(no of rows or pixels top to bottom) b is width(no of rows or pixels left to right) and 3 represents 3 rgb channels.... index 0 is red 1 is green 2 is blue

print(arr[0][0])#this will give us only the rgb value of the first pixel aka the top left pixel

print(arr[0][0][0])#only the red value for the first pixel

#Now that we have an idea of how the data is structured lets actually convert the img

R=arr[:,:,0]
G=arr[:,:,1] #we have extracted only the red green and blue values of all pixels, the : means all
B=arr[:,:,2] #what we are writing is basically all rows and all cols of this channels 0,1,2
gray=0.299*R + 0.587*G + 0.114*B #particular formula for conversion to greyscale... we are taking a weighted avg based on how heavily each colour is perceived by human eyes

print(gray.shape)#we only get a height and width now as the rgb values are merged into 1

#we are now only displaying the images and comparing the original and the grayscale

plt.figure(figsize=(10, 4))#allows for the images to have a fixed sizing 10 inches and 4 inches 

plt.subplot(1, 2, 1)#first row second col first index
plt.imshow(arr)#original
plt.axis("off")
plt.title("Original img")
#here indexing is from 0 btw
plt.subplot(1, 2, 2)#first row second col second index
plt.imshow(gray, cmap="gray")#so that it is recognized as gray
plt.axis("off")
plt.title("Grayscale img")

plt.show()


