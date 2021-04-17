import matplotlib.pyplot as plt
import matplotlib
import os 


class picture(): #klasa obrazów
    def __init__(self, id, matrix, name = None):
        self.id = id #id ma być zadawanie automatycznie przez inną funkcję
        self.matrix = matrix 
        
        if name == None: #Jeśli nazwa nie jest sprecyzowana -> nazwa = id
            self.name = id
        else:
            self.name = name
            
def save_as_image(A:object):
    
    directory = os.path.abspath('') #Ścieżka folderu
    
    print(directory)
    
    os.chdir(directory) #Ustawienie folderu, w którym zapisze się obraz
    
    if not os.path.exists(str(A.name)+'.png') : #Sprawdzenie, czy obraz już jest zapisany
        matplotlib.image.imsave(str(A.name)+'.png', A.matrix) #Zapisywanie
    else:
        print("Obraz już wcześniej został zapisany")
    
    pass
