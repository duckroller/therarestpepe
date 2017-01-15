from cv2 import *
import numpy as np
import random

img = "extension/pepe_meme.png"
img = imread(img)

def method_1(img):
    gray_image = cvtColor(img, COLOR_BGR2GRAY)
    return gray_image

def method_2(img):    #blur
    kernel_size = random.randint(5,15)
    edited = blur(img,(kernel_size,kernel_size))
    return edited

def method_3(img):  # Takes grayscale image
    kernel_size = random.randint(5,15)
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    iter_count = random.randint(1,5)
    erosion = erode(img,kernel,iterations = iter_count)
    return erosion

def method_4(img):  # Takes grayscale image
    #kernel = np.ones((5,5),np.uint8)
    kernel_size = random.randint(5,15)
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    iter_count = random.randint(1,5)
    dilation = dilate(img,kernel,iterations = iter_count)
    return dilation

def method_5(img):  # Takes grayscale image
    #kernel = np.ones((5,5),np.uint8)
    kernel_size = random.randint(5,15)
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    gradient = morphologyEx(img, MORPH_GRADIENT, kernel)
    return gradient

def method_6(img):  # Takes grayscale image
    kernel = np.ones((5,5),np.uint8)
    blackhat = morphologyEx(img, MORPH_BLACKHAT, kernel)
    return blackhat

def method_7(img): #inversion of colors
    inverted_img = bitwise_not(img)
    return inverted_img

methods = [method_2, method_3, method_4, method_5, method_6, method_7]

#m1 = method_1(img)
#imwrite("rare_1.png",m1)
#imwrite("rarest_2.png",method_2(img))
#imwrite("rarest_3a.png", method_3(img))    
#imwrite("rarest_4a.png", method_4(img))    
#imwrite("rarest_5a.png", method_5(img))    
#imwrite("rarest_6a.png", method_6(img))
#imwrite("rarest_7.png", method_7(img))
if __name__ == "__main__":
    try:
        first_permutation = random.choice(methods)(img) # 
        second_permutation = random.choice(methods)(first_permutation) 
        imwrite("rarest_pepe.png", second_permutation)
        print("Wohoo! You now have the rarest pepe in the world!")
    except:
        print("Something went wrong. Contact the developers.")