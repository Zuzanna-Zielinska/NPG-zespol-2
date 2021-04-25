import nonogram_test.zapis.interfejs_uzytkownika.gui_zapis as n
import numpy as np


# tutaj mozna zobaczyc jak dziala program
# odpala sie gui_zapis, zaznaczamy nasz wzor
# a po wcisnieciu przycisku "END" zamyka sie okno, a my
# mozemy wykorzystac otrzymana macierz.


# ponizej jest program wypisujacy otrzymana macierz
list_as_array = np.array(n.answer_nonogram)

print(list_as_array)
