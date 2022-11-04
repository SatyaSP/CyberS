import cv2
import string
import os

dict1 = {}
dict2 = {}
for i in range(255):
    dict1[chr(i)]=i
    dict2[i]=chr(i)

path=input("Enter image path : ")

img=cv2.imread(path)

key = input("Enter Your Secret Key : ")
text = input("Enter text to hide In the Image : ")
kl=0
x = 0 # No of rows
y = 0 # no of columns
z = 0 # plane selection
l=len(text)
print(f"Length of text : {l}")
for i in range(l):
    img[x, y, z] = dict1[text[i]] ^ dict1[key[kl]]
    y = y+1
    x = x+1
    x = (x+1)%3
    kl = (kl+1)%len(key)
    
cv2.imwrite("encryptedImage.jpg", img) 
os.startfile("encryptedImage.jpg")
print("Data Hiding in Image completed successfully.")