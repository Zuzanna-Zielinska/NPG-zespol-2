import gui_zapis as n
import numpy as np
import save_and_load as sv


# tutaj mozna zobaczyc jak dziala program
# odpala sie gui_zapis, zaznaczamy nasz wzor
# a po wcisnieciu przycisku "END" zamyka sie okno, a my
# mozemy wykorzystac otrzymana macierz.


# ponizej jest program wypisujacy otrzymana macierz
list_as_array = np.array(n.answer_nonogram)

print(list_as_array)

#Zapisywanie
sv.save_as_file(list_as_array, 'Stworzone_z_gui.pkl', 'Stworzone_z_gui.pkl')