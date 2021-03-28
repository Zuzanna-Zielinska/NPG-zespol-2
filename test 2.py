# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:33:54 2021

@author: Kiwi
"""

#pip install opencv-python #  <---  instalacja biblioteki cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt

A = np.ones([5, 5])
A[2][:] = 0

plt.imshow(A, 'gray')
plt.xticks([]), plt.yticks([])
plt.show()

B = np.ones([5, 5])

n1 = len(B)
n2 = len(B[0])

for i in range(n1):
    for j in range(n2):
        if i%2 == 0 and j%2 == 0:
            B[i][j] = 0
        elif i%2 == 1 and j%2 == 1:
            B[i][j] = 0

plt.imshow(B, 'gray')
plt.xticks([]), plt.yticks([])
plt.show()