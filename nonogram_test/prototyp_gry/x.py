        # Czyszczenie okna z elementow main menu
        self.clearwin()

        # Tworzenie okna rozgrywki
        self.canvas = Canvas(self.window, width=size_of_canvas, height=size_of_canvas, background=background_colour)
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
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid + size_of_outskirts, 0, i * size_of_grid + size_of_outskirts,
                                    size_of_board + size_of_outskirts, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid + size_of_outskirts, size_of_board + size_of_outskirts,
                                    i * size_of_grid + size_of_outskirts, width = 2)


    # Funckja wypisujaca macierz odpowiedzi
    def puzzle_info(self,nonogram):#TODO Optimalization of this function
        #columns
        ones_counter = 0
        columns = list(zip(*nonogram))
        array = []
        for i in range(size_of_nonogram):
            for j in range(size_of_nonogram):
                if not ones_counter - 1 == 0 and ones_counter > 0:
                    ones_counter -= 1
                    continue
                ones_counter = 0
                first_one = columns[i][j]
                if first_one == 1:
                    ones_counter = 1
                    for z in range(j+1,size_of_nonogram):
                        if columns[i][z] == 0:
                            break
                        else:
                            ones_counter+=1
                if not ones_counter == 0:
                    array.append(ones_counter)
            if not array == []:
                for j in range(len(array)):
                    self.canvas.create_text(size_of_outskirts+size_of_grid / 2 + size_of_grid * i,
                                            (j + 1) * size_of_font,font="Times 20",text = str(array[j]))
            array.clear()
        #rows
        ones_counter = 0
        rows = nonogram
        array = []
        for i in range(size_of_nonogram):
            for j in range(size_of_nonogram):
                if not ones_counter - 1 == 0 and ones_counter > 0:
                    ones_counter -= 1
                    continue
                ones_counter = 0
                first_one = rows[i][j]
                if first_one == 1:
                    ones_counter = 1
                    for z in range(j + 1, size_of_nonogram):
                        if rows[i][z] == 0:
                            break
                        else:
                            ones_counter += 1
                if not ones_counter == 0:
                    array.append(ones_counter)
            if not array == []:
                for j in range(len(array)):
                    self.canvas.create_text((j + 1) * size_of_font,size_of_outskirts + size_of_grid / 2 + size_of_grid * i,
                                            font="Times 20", text=str(array[j]))
            array.clear()
    # Funkcja zmieniajaca kolor kratki siatki oraz zmieniajaca macierz odpowiedzi
    def change_grid_status(self, click_position, x_clicked = False):

        #treating left upper corner like coords 0,0
        click_position[0]-=size_of_outskirts
        click_position[1]-=size_of_outskirts

        # Check if the click was outside board
        if click_position[0] < 0 or click_position[1] < 0:
            return
        if click_position[0] > size_of_board or click_position[1] > size_of_board:
            return

        # Wyznaczenie, w ktorej kratce mialo miejsce klikniecie
        for i in range(size_of_nonogram + 1):
            if click_position[0] <= i * size_of_grid and click_position[0] >= (i - 1) * size_of_grid:
                # x coords of left upper corner of clicked square
                x_position = (i - 1) * size_of_grid + size_of_outskirts
                # column containing clicked square
                col = i - 1
                break
        for i in range(size_of_nonogram + 1):
            if click_position[1] <= i * size_of_grid and click_position[1] >= (i - 1) * size_of_grid:
                # y coords of left upper corner of clicked square
                y_position = (i - 1) * size_of_grid + size_of_outskirts
                # row containing clicked square
                row = i - 1
                break

        # kliknieto prawy przycisk (x), Zmiana macierzy odpowiedzi i wypelnienie komórki
        if x_clicked:
            if self.answer_nonogram[row][col] == 0:
                self.answer_nonogram[row][col] = 2
                self.canvas.create_line(x_position, y_position, x_position + size_of_grid, y_position + size_of_grid, width=4, fill = marked_grid_colour)
                self.canvas.create_line(x_position + size_of_grid, y_position , x_position, y_position + size_of_grid, width=4, fill=marked_grid_colour)
                return
            elif self.answer_nonogram[row][col] == 2:
                self.answer_nonogram[row][col] = 0
                self.canvas.create_rectangle(x_position, y_position, x_position + size_of_grid,
                                             y_position + size_of_grid, fill=background_colour)
                return
            else:
                return

        # Zmiana macierzy odpowiedzi
        if self.answer_nonogram[row][col] == 0:
            self.answer_nonogram[row][col] = 1
            self.canvas.create_rectangle(x_position, y_position, x_position + size_of_grid, y_position + size_of_grid, fill = marked_grid_colour)
        else:
            self.answer_nonogram[row][col] = 0
            self.canvas.create_rectangle(x_position,y_position,x_position + size_of_grid,y_position + size_of_grid, fill = background_colour)

    # Funkcja sprawdzajaca czy macierz odpowiedzi jest identyczna z nonogramem
    def check_win(self):
        if (self.nonogram == self.answer_nonogram).all():
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
        for i in range(size_of_nonogram):
            for j in range(size_of_nonogram):
                if self.nonogram[i][j] == 1:
                    self.canvas.create_rectangle(j * size_of_nonogram * 2, i * size_of_nonogram * 2, (j + 1) * size_of_nonogram * 2,
                                                 (i + 1) * size_of_nonogram * 2, fill=marked_grid_colour)

        # Rysowanie siatki oraz wypisywanie tekstu
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid, 0, i * size_of_grid, size_of_board, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid, size_of_board, i * size_of_grid, width = 2)

        self.canvas.create_text(size_of_board / 2, size_of_board + 100,
                                text="Naciśnij enter aby wrócić do menu", font=('Comic Sans MS', 19, 'bold italic'))

    # Funkcja obslugujaca klinkniecie gracza w trakcie rozgrywki
    def click(self, event):
        if self.in_game == True:
            # coords of click
            click_position = [event.x, event.y]
            # Zmiana statusu macierzy odpowiedzi, kolorowanie siatki
            self.change_grid_status(click_position, False)
            # Sprawdzanie wygranej
            self.win = self.check_win()

            self.initialize_nonogram()#used to keep thick lines

            # Czynnosci podjete w wypadku wygranej
            if self.win == True:
                self.canvas.create_text(size_of_outskirts / 2,size_of_outskirts / 2, text = "Wygrałeś!",
                                        font=('Comic Sans MS', 19, 'bold italic'))
                self.canvas.create_text(size_of_outskirts / 2, size_of_outskirts / 2 + 30,
                 text="Naciśnij enter aby kontynuować", font=('Comic Sans MS', 8, 'bold italic'))
                sv.change_to_solved(True,self.chosen_level.id,"Obrazy.pkl")

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
