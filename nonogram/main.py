from tkinter import filedialog
from tkinter import *
import numpy as np
import os
import save_and_load as sv


# Wymiary okna gry i siatki


# kolory zaznaczonych oraz odznaczonych kratek
marked_grid_colour = '#444444'
background_colour = '#F5F5F5'
X_colour = '#db2918'


class Nonogram():
    # Initialization functions
    def __init__(self):
        self.window = Tk()
        self.window.title('Nonogram')

        self.graphic_theme = sv.load_list_from_file('Motywy.pkl')[0]
        self.theme_dictionary = {"Kot patrzący w dal" : "cat_and_window.ppm",
                                 "Miasto w nocy" : "town.ppm",
                                 "Róża" : "rose.ppm"}
        self.button_theme = sv.load_list_from_file('Motywy.pkl')[1]
        self.button_theme_dictionary = {"Kot patrzący w dal" : ['papaya whip', 'OrangeRed4'],
                                 "Miasto w nocy" : ['papaya whip', 'burlywood2'],
                                 "Róża" : ['papaya whip', 'aquamarine4']}
        self.font_theme = ['Harlow Solid Italic', 'Goudy Old Style', 'Goudy Old Style', 'Lucida Handwriting', 'Forte']

        self.main_menu()


    def define_sizes(self,nonogram):
        self.size_of_nonogram = len(nonogram[0])
        self.size_of_grid = 30
        self.size_of_board = self.size_of_nonogram * self.size_of_grid
        self.size_of_canvas = 700
        self.size_of_outskirts = 6 * self.size_of_grid
        self.size_of_font = 30

    def chose_theme(self):
        self.in_menu = False

        self.clearwin()

        # Tworzenie przestrzeni oraz wypelnianie obrazkiem, dodawanie tekstu
        self.canvas = Canvas(self.window, width=550, height=840)
        self.canvas.pack()

        self.main_menu_image = PhotoImage(
            file=self.graphic_theme)  # podobno png mialy nie dzialac wiec ich nie uzywam choc dzialaja
        self.image = self.canvas.create_image(550, 0, anchor=NE, image=self.main_menu_image)

        self.canvas.create_text(274, 49,fill = 'white', text="Wybór tla", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(274, 51,fill = 'white', text="Wybór tla", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(276, 51,fill = 'white', text="Wybór tla", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(276, 49,fill = 'white', text="Wybór tla", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(275, 50,fill = 'black', text="Wybór tla", font=(self.font_theme[1], 20, 'bold italic'))

        # Tworzenie listy
        self.listbox = Listbox(self.window, width=30, height=30)
        self.listbox.place(x=175, y=100, in_=self.window)

        self.listbox.insert(END, "Kot patrzący w dal")
        self.listbox.insert(END, "Miasto w nocy")
        self.listbox.insert(END, "Róża")

        # Przycisk do wybrania, po nacisnieciu przekazuje wybrany nonogram do zmiennej i zaczyna gre
        self.button_options_menu = Button(self.window, command=lambda: self.choose_theme_menu_click(), text="Wybierz",
                                          font=(self.font_theme[2], 15, 'bold italic'), background = self.button_theme[0])
        self.button_options_menu.place(x=220, y=600, in_=self.window)

        # Przycisk wracajacy do menu
        self.return_to_menu = Button(self.window, command=lambda: self.back_to_menu(), text="Powrot do menu",
                                     width=20, height=1, bd=5, font=(self.font_theme[2], 10, 'bold italic'), background = self.button_theme[0])
        self.return_to_menu.place(x=180, y=660, in_=self.window)

        # Druga, alternatywna opcja wyboru
        self.listbox.bind('<Double-Button>', lambda x: self.choose_theme_menu_click())

    # Funckja obslugujaca menu wyboru poziomu
    def choose_level_menu(self):
        self.in_options = True
        self.in_menu = False

        self.clearwin()

        # Tworzenie przestrzeni oraz wypelnianie obrazkiem, dodawanie tekstu
        self.canvas = Canvas(self.window, width=550, height=840)
        self.canvas.pack()

        self.main_menu_image = PhotoImage(
            file=self.graphic_theme)  # podobno png mialy nie dzialac wiec ich nie uzywam choc dzialaja
        self.image = self.canvas.create_image(550, 0, anchor=NE, image=self.main_menu_image)

        self.canvas.create_text(274, 49,fill = 'white', text="Wybór poziomu", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(274, 51,fill = 'white', text="Wybór poziomu", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(276, 51,fill = 'white', text="Wybór poziomu", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(276, 49,fill = 'white', text="Wybór poziomu", font=(self.font_theme[1], 20, 'bold italic'))
        self.canvas.create_text(275, 50,fill = 'black', text="Wybór poziomu", font=(self.font_theme[1], 20, 'bold italic'))

        # Tworzenie listy
        self.listbox = Listbox(self.window, width = 30, height = 30)
        self.listbox.place(x = 175, y = 100, in_ = self.window)


        # Wypełnianie listy nonogrami z stoworze_z_gui.pkl
        self.flist = sv.id_and_name_list(sv.load_list_from_file("Stworzone_z_gui.pkl"))
        for item in self.flist:
            self.listbox.insert(END, item)

        # Przycisk do wybrania, po nacisnieciu przekazuje wybrany nonogram do zmiennej i zaczyna gre
        self.button_options_menu = Button(self.window, command = lambda: self.choose_level_menu_click(), text ="Wybierz",
                                          font = (self.font_theme[2], 15, 'bold italic'), background = self.button_theme[0])
        self.button_options_menu.place(x = 220, y = 600, in_ = self.window)

        # Przycisk wracajacy do menu
        self.return_to_menu = Button(self.window, command=lambda: self.back_to_menu(), text="Powrot do menu",
                                     width=20, height=1, bd=5, font=(self.font_theme[2], 10, 'bold italic'), background = self.button_theme[0])
        self.return_to_menu.place(x=180, y=660, in_=self.window)

        # Druga, alternatywna opcja wyboru
        self.listbox.bind('<Double-Button>', lambda x: self.choose_level_menu_click())

    # Funckja przekazuje wybrany nonogram do zmiennej i wraca do main menu
    def choose_level_menu_click(self):

        # Nazwa pliku
        self.name_of_nonongram = (self.listbox.get(self.listbox.curselection()[0]))

        # Tworzenie sciezki do wybranego pliku
        self.chosen_level = sv.load_one_from_file(self.name_of_nonongram, "Stworzone_z_gui.pkl")

        # Zaladowanie pliku do zmiennej
        self.nonogram = self.chosen_level.matrix

        self.start_game(self.nonogram)

        # Wyjscie do main menu stare
        #self.clearwin()
        #self.main_menu()
    def choose_theme_menu_click(self):


        # Nazwa pliku
        self.chosen_theme = (self.listbox.get(self.listbox.curselection()))
        self.graphic_theme = self.theme_dictionary[self.chosen_theme]
        self.button_theme = self.button_theme_dictionary[self.chosen_theme]
        sv.save_object([self.graphic_theme, self.button_theme], 'Motywy.pkl')

        self.back_to_menu()

    # Funkcja obslugujaca main menu
    def main_menu(self):
        self.in_menu = True
        self.in_game = False

        # Tworzenie przestrzeni oraz wypelnianie obrazkiem, dodawanie tekstu i przyciskow
        self.canvas = Canvas(self.window, width = 550, height = 840)
        self.canvas.pack()

        self.main_menu_image = PhotoImage(file=self.graphic_theme)# podobno png mialy nie dzialac wiec ich nie uzywam choc dzialaja
        self.image = self.canvas.create_image(550, 0, anchor=NE, image=self.main_menu_image)

        self.canvas.create_text(273, 78, fill = 'white', text = "Nonogram game", font = (self.font_theme[0], 50, 'bold italic'))
        self.canvas.create_text(273, 82, fill = 'white', text = "Nonogram game", font = (self.font_theme[0], 50, 'bold italic'))
        self.canvas.create_text(277, 82, fill = 'white', text = "Nonogram game", font = (self.font_theme[0], 50, 'bold italic'))
        self.canvas.create_text(277, 78, fill = 'white', text = "Nonogram game", font = (self.font_theme[0], 50, 'bold italic'))
        self.canvas.create_text(275, 80, fill = 'black', text = "Nonogram game", font = (self.font_theme[0], 50, 'bold italic'))

        # Definiowanie i dodawanie przyciskow
        # Przycisk do wyjscia (niegotowy)
        self.exit_button = Button(self.window, command = lambda: self.window.destroy(), text = 'WYJSCIE', width = 10,
                                   height = 1, bd = 5, font = (self.font_theme[2], 35, 'bold italic'), background = self.button_theme[0])
        self.exit_button.place(x = 120, y = 570, in_ = self.window)

        # Przycisk do wejscia do opcji (niegotowy)
        self.option_button = Button(self.window, command = lambda: self.options_menu(), text = 'OPCJE', width=10,
                                   height = 1, bd = 5, font = (self.font_theme[2], 35, 'bold italic'), background = self.button_theme[0])
        self.option_button.place(x=120, y=370, in_=self.window)

        # Przycisk do startu gry
        self.start_button = Button(self.window, command = lambda: self.choose_level_menu(), text ='GRAJ', width = 10,
                                   height = 1, bd = 5, font = (self.font_theme[2], 35, 'bold italic'), background = self.button_theme[0])
        self.start_button.place(x=120, y=170, in_=self.window)

        # Przycisk do wyboru poziomow z poziomu eksploratora za pomoca funkcji set_nonogram DEBUG

        self.debug_button = Button(self.window, command=lambda: self.set_nonogram(), text='DEBUG', width=10,
                                    height=1, bd=5, font=(self.font_theme[2], 10, 'bold italic'), background = self.button_theme[1])
        self.debug_button.place(x=10, y=10, in_=self.window)

        # Przycisk startujacy w trybie DEBUG
        self.start_button = Button(self.window, command=lambda: self.start_game(self.nonogram), text='DEBUG_START', width=15,
                                   height=1, bd=5, font=(self.font_theme[2], 10, 'bold italic'), background = self.button_theme[1])
        self.start_button.place(x=120, y=10, in_=self.window)

    # Funkcja obslugujaca menu opcji
    def options_menu(self):
        self.in_options = True
        self.in_menu = False

        self.clearwin()

        # Tworzenie przestrzeni oraz wypelnianie obrazkiem, dodawanie tekstu
        self.canvas = Canvas(self.window, width=550, height=840)
        self.canvas.pack()

        self.main_menu_image = PhotoImage(
            file=self.graphic_theme)  # podobno png mialy nie dzialac wiec ich nie uzywam choc dzialaja
        self.image = self.canvas.create_image(550, 0, anchor=NE, image=self.main_menu_image)

        self.canvas.create_text(274, 49, fill = 'white', text="OPCJE", font=(self.font_theme[1], 30, 'bold italic'))
        self.canvas.create_text(274, 51, fill = 'white', text="OPCJE", font=(self.font_theme[1], 30, 'bold italic'))
        self.canvas.create_text(276, 51, fill = 'white', text="OPCJE", font=(self.font_theme[1], 30, 'bold italic'))
        self.canvas.create_text(276, 49, fill = 'white', text="OPCJE", font=(self.font_theme[1], 30, 'bold italic'))
        self.canvas.create_text(275, 50, fill = 'black', text="OPCJE", font=(self.font_theme[1], 30, 'bold italic'))

        self.reset_button = Button(self.window, command = lambda: sv.change_all_to_unsolved("stworzone_z_gui.pkl"),
                                   text = 'Resetuj postepy', width = 20, height = 1, bd = 5,
                                   font=(self.font_theme[2], 20, 'bold italic'), background = self.button_theme[0])
        self.reset_button.place(x=100, y=200, in_=self.window)

        self.chose_theme_button = Button(self.window, command=lambda: self.chose_theme(),
                                   text='Zmien tlo', width=20, height=1, bd=5,
                                   font=(self.font_theme[2], 20, 'bold italic'), background = self.button_theme[0])
        self.chose_theme_button.place(x=100, y=300, in_=self.window)

        self.return_to_menu = Button(self.window, command = lambda: self.back_to_menu(), text='Powrot',
                                     width=20, height=1, bd=5, font=(self.font_theme[2], 20, 'bold italic'), background = self.button_theme[0])
        self.return_to_menu.place(x=100, y=600, in_=self.window)

    # Funckja wracajaca do menu
    def back_to_menu(self):
        self.clearwin()
        self.main_menu()

    # Funkcja umozliwiajaca wybor poziomow z poziomu ekploratora
    def set_nonogram(self):
        # Dopuszczalne typy plikow
        self.my_filetypes = [('Nonogramy', '.npy')]

        # Sciezka do wybranego pliku
        self.chosen_level = filedialog.askopenfilename(parent=self.window,
                                                       initialdir=os.getcwd() + '\\Nonograms',
                                                       title="Please select a file:",
                                                       filetypes=self.my_filetypes)

        # Ladowanie wybranego pliku do zmiennej nonogram
        self.nonogram = np.load(self.chosen_level)

    # Funkcja rozpoczynajaca rozgrywke, musi dostac nonogram
    def start_game(self,nonogram):
        self.in_menu = False
        self.in_game = True

        self.define_sizes(nonogram)

        #nonogram ktory bedzie wypelniany przez gracza
        self.answer_nonogram = np.zeros((self.size_of_nonogram, self.size_of_nonogram), dtype=int)

        #nonogram wypelniany przez gracza bez znakow x
        self.check_win_nonogram = np.zeros((self.size_of_nonogram, self.size_of_nonogram), dtype=int)

        # Czyszczenie okna z elementow main menu
        self.clearwin()

        # Tworzenie okna rozgrywki
        self.canvas = Canvas(self.window, width=self.size_of_canvas, height=self.size_of_canvas, background=background_colour)
        self.canvas.pack()

        # Mozliwe interakcje od gracza
        #LPM
        self.window.bind('<Button-1>', self.click)

        # Wstawianie x
        self.window.bind('<Button-3>', self.click_x)

        # Enter
        self.window.bind('<Return>', self.end_game)

        # Wywolanie funkcji rysujacej siatke oraz wypisujacej macierz odpowiedzi
        self.initialize_nonogram()
        self.puzzle_info(nonogram)
        self.win = False
        self.exit = False
        self.game_finished = False

    # Funkcja czysci okno z wszelkich elementow
    def clearwin(self):
        for child in self.window.winfo_children():
            child.destroy()
    # Petla programu
    def mainloop(self):
        self.window.mainloop()

    # Funkcja rysuje siatke nonogramu
    def initialize_nonogram(self):
        for i in range(self.size_of_nonogram + 1):
            self.canvas.create_line(i * self.size_of_grid + self.size_of_outskirts, 0, i * self.size_of_grid + self.size_of_outskirts,
                                    self.size_of_board + self.size_of_outskirts, width = 2)

        for i in range(self.size_of_nonogram + 1):
            self.canvas.create_line(0, i * self.size_of_grid + self.size_of_outskirts, self.size_of_board + self.size_of_outskirts,
                                    i * self.size_of_grid + self.size_of_outskirts, width = 2)


    # Funckja wypisujaca macierz odpowiedzi
    def puzzle_info(self,nonogram):#TODO Optimalization of this function
        #columns
        ones_counter = 0
        columns = list(zip(*nonogram))
        array = []
        for i in range(self.size_of_nonogram):
            for j in range(self.size_of_nonogram):
                if not ones_counter - 1 == 0 and ones_counter > 0:
                    ones_counter -= 1
                    continue
                ones_counter = 0
                first_one = columns[i][j]
                if first_one == 1:
                    ones_counter = 1
                    for z in range(j+1,self.size_of_nonogram):
                        if columns[i][z] == 0:
                            break
                        else:
                            ones_counter+=1
                if not ones_counter == 0:
                    array.append(ones_counter)
            if not array == []:
                for j in range(len(array)):
                    self.canvas.create_text(self.size_of_outskirts+self.size_of_grid / 2 + self.size_of_grid * i,
                                            (j + 1) * self.size_of_font,font="Times 20",text = str(array[j]))
            array.clear()
        #rows
        ones_counter = 0
        rows = nonogram
        array = []
        for i in range(self.size_of_nonogram):
            for j in range(self.size_of_nonogram):
                if not ones_counter - 1 == 0 and ones_counter > 0:
                    ones_counter -= 1
                    continue
                ones_counter = 0
                first_one = rows[i][j]
                if first_one == 1:
                    ones_counter = 1
                    for z in range(j + 1, self.size_of_nonogram):
                        if rows[i][z] == 0:
                            break
                        else:
                            ones_counter += 1
                if not ones_counter == 0:
                    array.append(ones_counter)
            if not array == []:
                for j in range(len(array)):
                    self.canvas.create_text((j + 1) * self.size_of_font,
                                            self.size_of_outskirts + self.size_of_grid / 2 + self.size_of_grid * i,
                                            font="Times 20", text=str(array[j]))
            array.clear()
    # Funkcja zmieniajaca kolor kratki siatki oraz zmieniajaca macierz odpowiedzi
    def change_grid_status(self, click_position, x_clicked = False):

        #treating left upper corner like coords 0,0
        click_position[0]-=self.size_of_outskirts
        click_position[1]-=self.size_of_outskirts

        # Check if the click was outside board
        if click_position[0] < 0 or click_position[1] < 0:
            return
        if click_position[0] > self.size_of_board or click_position[1] > self.size_of_board:
            return



        # Wyznaczenie, w ktorej kratce mialo miejsce klikniecie
        for i in range(self.size_of_nonogram + 1):
            if click_position[0] <= i * self.size_of_grid and click_position[0] >= (i - 1) * self.size_of_grid:
                # x coords of left upper corner of clicked square
                x_position = (i - 1) * self.size_of_grid + self.size_of_outskirts
                # column containing clicked square
                col = i - 1
                break
        for i in range(self.size_of_nonogram + 1):
            if click_position[1] <= i * self.size_of_grid and click_position[1] >= (i - 1) * self.size_of_grid:
                # y coords of left upper corner of clicked square
                y_position = (i - 1) * self.size_of_grid + self.size_of_outskirts
                # row containing clicked square
                row = i - 1
                break

        # kliknieto prawy przycisk (x), Zmiana macierzy odpowiedzi i wypelnienie komórki
        if x_clicked:
            if self.answer_nonogram[row][col] == 0:
                self.answer_nonogram[row][col] = 2
                self.canvas.create_line(x_position + 3, y_position + 3, x_position + self.size_of_grid - 3,
                                        y_position + self.size_of_grid - 3, width=4, fill=X_colour)
                self.canvas.create_line(x_position + self.size_of_grid - 3, y_position + 3, x_position + 3,
                                        y_position + self.size_of_grid - 3, width=4, fill=X_colour)
                return
            elif self.answer_nonogram[row][col] == 2:
                self.answer_nonogram[row][col] = 0
                self.canvas.create_rectangle(x_position, y_position, x_position + self.size_of_grid,
                                             y_position + self.size_of_grid, fill=background_colour)
                return
            else:
                return

        # Zmiana macierzy odpowiedzi
        if self.answer_nonogram[row][col] == 0:
            self.answer_nonogram[row][col] = 1
            self.check_win_nonogram[row][col] = 1
            self.canvas.create_rectangle(x_position, y_position, x_position + self.size_of_grid, y_position + self.size_of_grid, fill = marked_grid_colour)
        elif self.answer_nonogram[row][col] == 2:
            return
        else:
            self.answer_nonogram[row][col] = 0
            self.check_win_nonogram[row][col] = 0
            self.canvas.create_rectangle(x_position,y_position,x_position + self.size_of_grid,y_position + self.size_of_grid, fill = background_colour)

    # Funkcja sprawdzajaca czy macierz odpowiedzi jest identyczna z nonogramem
    def check_win(self):
        if (self.nonogram == self.check_win_nonogram).all():
            return True

        return False

    # Funckja realizujaca koniec pojedynczego nonogramu oraz powrot do main menu
    def end_game(self,event):
        if self.win == True:
            self.in_game = False

            # Czyszczenie okna z gra, pozostawienie przestrzeni
            self.canvas.delete("all")

            # Rysowanie rozwiazanego nonogramu
            self.print_nonogram()
            self.game_finished = True
            self.win = False
            return
        if self.game_finished == True:
            # Czyszczenie okna, powrot do menu
            self.clearwin()
            self.main_menu()

    # Funkcja rysujaca wypelniony nonogram
    def print_nonogram(self):
        # Rysowanie wypelnionych pol
        for i in range(self.size_of_nonogram):
            for j in range(self.size_of_nonogram):
                if self.nonogram[i][j] == 1:
                    self.canvas.create_rectangle(j * self.size_of_grid, i * self.size_of_grid,
                                                 (j + 1) * self.size_of_grid,
                                                 (i + 1) * self.size_of_grid, fill=marked_grid_colour)

        # Rysowanie siatki oraz wypisywanie tekstu
        for i in range(self.size_of_nonogram + 1):
            self.canvas.create_line(i * self.size_of_grid, 0, i * self.size_of_grid, self.size_of_board, width = 2)

        for i in range(self.size_of_nonogram + 1):
            self.canvas.create_line(0, i * self.size_of_grid, self.size_of_board, i * self.size_of_grid, width = 2)

        self.canvas.create_text(self.size_of_board / 2, self.size_of_board + 100,
                                text="Naciśnij enter aby wrócić do menu", font=(self.font_theme[1], 19, 'bold italic'))

    # Funkcja obslugujaca klinkniecie gracza w trakcie rozgrywki
    def click(self, event):
        if self.in_game == True:
            # coords of click
            click_position = [event.x, event.y]
            # Zmiana statusu macierzy odpowiedzi, kolorowanie siatki
            self.change_grid_status(click_position)
            # Sprawdzanie wygranej
            self.win = self.check_win()

            self.initialize_nonogram()#used to keep thick lines

            # Czynnosci podjete w wypadku wygranej
            if self.win == True:
                self.canvas.create_text(self.size_of_outskirts / 2,self.size_of_outskirts / 2, text = "Wygrałeś!",
                                        font=(self.font_theme[1], 19, 'bold italic'))
                self.canvas.create_text(self.size_of_outskirts / 2, self.size_of_outskirts / 2 + 30,
                 text="Naciśnij enter aby kontynuować", font=(self.font_theme[1], 8, 'bold italic'))
                sv.change_to_solved(True,self.chosen_level.id,"Stworzone_z_gui.pkl")

    def click_x(self, event):
        if self.in_game == True:
            # informacaj, ze kliknieto x
            x_clicked = True
            # coords of click
            click_position = [event.x, event.y]
            # Rysowanie X
            self.change_grid_status(click_position, x_clicked)

            self.initialize_nonogram()  # used to keep thick lines




game_instance = Nonogram()
game_instance.mainloop()
