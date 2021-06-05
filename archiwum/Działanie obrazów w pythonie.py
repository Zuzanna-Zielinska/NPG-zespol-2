#pip install opencv-python #  <---  instalacja biblioteki cv2

import numpy as np                  #Załączenie biblioteki funkcji do macierzy
import matplotlib.pyplot as plt     #Załączenie biblioteki do wywietlania wykresów

A = np.ones([5, 5])                 #Tworzenie macierzy jedynek
A[2][:] = 0                         #Wypełnienie drugiego wiersza zerami

plt.imshow(A, 'gray')               #Wywietlenie obrazka A w skali szarości
plt.xticks([]), plt.yticks([])
plt.show()

B = np.ones([5, 5])                 #Tworzenie macierzy jedynek

n1 = len(B)
n2 = len(B[0])

for i in range(n1):                 #Tworzenie szachownicy
    for j in range(n2):
        if i%2 == 0 and j%2 == 0:
            B[i][j] = 0
        elif i%2 == 1 and j%2 == 1:
            B[i][j] = 0

plt.imshow(B, 'gray')               #Wywietlenie obrazka B w skali szarości
plt.xticks([]), plt.yticks([])
plt.show()