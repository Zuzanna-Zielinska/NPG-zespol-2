import matplotlib
import os 
import pickle
from typing import List

#----------------klasa obrazów---------------------------
class picture(): 
    def __init__(self, id, matrix, name = None, is_solved = False):
        self.id = id #id ma być zadawanie automatycznie przez inną funkcję
        self.matrix = matrix 
        
        if name == None: #Jeśli nazwa nie jest sprecyzowana -> nazwa = id
            self.name = id
        else:
            self.name = name
        
        self.is_solved = is_solved
            
#----------------baza zapisu picture jako obrazka---------------------------
def save_as_image(A: object):
    
    directory = os.path.abspath('') #Ścieżka folderu
    
    print(directory)
    
    os.chdir(directory) #Ustawienie folderu, w którym zapisze się obraz
    
    if not os.path.exists(str(A.name)+'.png') : #Sprawdzenie, czy obraz już jest zapisany
        matplotlib.image.imsave(str(A.name)+'.png', A.matrix) #Zapisywanie
    else:
        print("Obraz już wcześniej został zapisany")
    
    pass

#-------Pomocnicza fukcja, używana tylko w innych funkcjach-------
def save_object(obj: object, filename: str): 
    with open(filename, 'wb') as output:  # Jeśli plik istnieje, to go nadpisuje, jeśli nie, to go tworzy
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#---Wczytuje stare dane, dodaje element, nadpisuje dane + automatycznie nadaje id---
def save_as_file(new_pictures_matrix: List[List[int]], new_file_name: str, old_file_name: str = 'None', new_pictures_name: str = 'None'): 
    
    if not os.path.isfile(old_file_name) or old_file_name == 'None': #Sprawdzanie czy pierwotny plik istnieje
        if new_pictures_name != 'None': #Tworzenie obiektu picture
            new_picture = picture(0, new_pictures_matrix, new_pictures_name)
        else:
            new_picture = picture(0, new_pictures_matrix)
        save_object([new_picture], new_file_name)
        return None
    
    with open(old_file_name, 'rb') as input: #Wczytywanie danych
        p = pickle.load(input)
        
    n = len(p) #Id zaczyna się od zera, więc id nowego elementu, to długość starej listy
    
    if new_pictures_name != 'None': #Tworzenie obiektu picture
        new_picture = picture(n, new_pictures_matrix, new_pictures_name)
    else:
        new_picture = picture(n, new_pictures_matrix)
    
    p.append(new_picture)
    save_object(p, new_file_name)
    
    return None

#-------Funkcja do wczytywania jednego obiektu z pliku wybieranego po id-------
def load_one_from_file(id: int, file_name: str) -> object:
    
    with open(file_name, 'rb') as input: #Wczytywanie danych
        pictures = pickle.load(input)
        
    for p in pictures: #Szukanie włściwego id
        if p.id == id:
            return p
            
    print("Plik o id = "+str(id)+" nie istnieje.")
    return None

#-------Funkcja do wczytywania wszystkich obiektów z pliku-------
def load_list_from_file(file_name: str) -> List[object]:
    
    with open(file_name, 'rb') as input: #Wczytywanie danych
        pictures = pickle.load(input)
    
    return pictures

#-------Pomocnicza fukcja do kopiowania plików-------
def copy_file(new_file_name:str, old_file_name: str):
    
    with open(old_file_name, 'rb') as input: #Wczytywanie danych
        p = pickle.load(input)
        
    save_object(p, new_file_name) #Zapis
    
    pass

#-------Pomocnicza fukcja do kopiowania plików-------
def change_to_solved(id: int, file_name: str):
    
    with open(file_name, 'rb') as input: #Wczytywanie danych
        pictures = pickle.load(input)
    
    for p in pictures: #Szukanie włściwego id i oznaczenie jako uzupełnionego
        if p.id == id:
            p.is_solved = True
    
    save_object(pictures, file_name) #Zapis
    
    if id >= len(pictures):
        print("Plik o id = "+str(id)+" nie istnieje.")
    
    pass