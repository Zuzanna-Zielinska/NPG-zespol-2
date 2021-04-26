import save_and_load as sv

#----Deklaracja macierzy----
p1 = [[1, 0], [1, 0]]

nonogram=[[1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
          [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1],
          [1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
          [1,0,1,1,0,0,0,1,0,0,0,1,1,0,1],
          [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
          [0,1,1,1,1,0,0,1,0,0,1,1,1,1,0],
          [0,1,1,1,1,0,0,1,0,0,1,1,1,1,0],
          [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
          [0,1,1,1,1,1,1,0,1,1,1,1,1,1,0],
          [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
          [1,0,1,1,0,0,0,0,0,0,0,1,1,0,1],
          [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
          [1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
          [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1],
          [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1]]

p3 = [[0, 1], [0, 1]]

#----Zapisywanie kolejnych macierzy w jednym pliku----
sv.save_as_file(p1, 'Obrazy.pkl', 'None', "Krotka")
sv.save_as_file(nonogram, 'Obrazy.pkl', 'Obrazy.pkl', "Wrotka")
sv.save_as_file(p3, 'Obrazy.pkl', 'Obrazy.pkl', "Stokrotka")
sv.save_as_file(p1, 'Obrazy.pkl', 'Obrazy.pkl')

#----Ładowanie kolejnych macierzy----
p = sv.load_one_from_file(0, 'Obrazy.pkl')
print(p.name)
p = sv.load_one_from_file(1, 'Obrazy.pkl')
print(p.name)
p = sv.load_one_from_file(2, 'Obrazy.pkl')
print(p.name)
p = sv.load_one_from_file(3, 'Obrazy.pkl')
print(p.name)
p = sv.load_one_from_file(10, 'Obrazy.pkl')
print(p)

print(" ")

#----Ładowanie wszystkich macierzy z pliku----
lst = sv.load_list_from_file('Obrazy.pkl')
print(lst[0].name)

print(" ")

#----Kopiowanie plików----
sv.copy_file('Obrazy_wypełniane.pkl', 'Obrazy.pkl')
p = sv.load_list_from_file('Obrazy_wypełniane.pkl')
print(p[1].is_solved)

#----Oznaczenie jednego obrazka jako rozwiązanego----
sv.change_to_solved(1 ,'Obrazy_wypełniane.pkl')
p = sv.load_list_from_file('Obrazy_wypełniane.pkl')
print(p[1].is_solved)