import save_and_load as sv

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
sv.save_as_file(p1, 'Obrazy.pkl', 'None', "Krotka")
sv.save_as_file(nonogram, 'Obrazy.pkl', 'Obrazy.pkl', "Wrotka")
sv.save_as_file(p3, 'Obrazy.pkl', 'Obrazy.pkl', "Stokrotka")
sv.save_as_file(p1, 'Obrazy.pkl', 'Obrazy.pkl')

p = sv.load_from_file(0, 'Obrazy.pkl')
print(p.name)

p = sv.load_from_file(1, 'Obrazy.pkl')
print(p.name)

p = sv.load_from_file(2, 'Obrazy.pkl')
print(p.name)

p = sv.load_from_file(3, 'Obrazy.pkl')
print(p.name)

p = sv.load_from_file(10, 'Obrazy.pkl')
print(p)