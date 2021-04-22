from tkinter import filedialog
from tkinter import *
import numpy as np
import os

size_of_nonogram = 15
size_of_grid = 30
size_of_board = size_of_nonogram*size_of_grid
size_of_canvas = 700
size_of_outskirts = 6 * size_of_grid
size_of_font = 30


marked_grid_colour = '#444444'
background_colour = '#F5F5F5'

test = 'nonogram_test.npy'
wikipedia = 'nonogram_wikipedia.npy'

class Nonogram():
    #Initialization functions
    def __init__(self):
        self.window = Tk()
        self.window.title('Nonogram')

        self.main_menu()

    def main_menu(self):
        self.in_menu = True

        self.canvas = Canvas(self.window, width = 551, height = 826)
        self.canvas.pack()

        self.main_menu_image = PhotoImage(file="main_menu_image.ppm")#podobno png mialy nie dzialac wiec ich nie uzywam choc dzialaja
        self.image = self.canvas.create_image(551, 0, anchor=NE, image=self.main_menu_image)

        self.canvas.create_text(275, 80, text = "Nongram game", font = ('Comic Sans MS', 50, 'bold italic'))

        self.start_button = Button(self.window, command = lambda: self.start_game(self.nonogram), text = 'START', width = 10,
                                   height = 1, bd = 5, font = ('Comic Sans MS', 40, 'bold italic'))
        self.start_button.place(x = 110, y = 200, in_ = self.window)

        self.option_button = Button(self.window, command = lambda: self.set_nonogram(), text = 'OPCJE', width=10,
                                   height = 1, bd = 5, font = ('Comic Sans MS', 40, 'bold italic'))
        self.option_button.place(x=110, y=400, in_=self.window)

        # Na razie nie ma tu zadnej funkcji, takie samo dzialanie jak start button
        self.sth_button = Button(self.window, command = lambda: self.start_game(self.nonogram), text = 'STH', width = 10,
                                   height = 1, bd = 5, font = ('Comic Sans MS', 40, 'bold italic'))
        self.sth_button.place(x=110, y=600, in_=self.window)

    def set_nonogram(self):
        self.game_path = os.getcwd()
        self.nonograms_path = self.game_path + '\\Nonograms'
        self.my_filetypes = [('Nonogramy', '.npy')]
        self.answer = filedialog.askopenfilename(parent=self.window,
                                            initialdir=self.nonograms_path,
                                            title="Please select a file:",
                                            filetypes=self.my_filetypes)
        self.nonogram = np.load(self.answer)

    def start_game(self,nonogram):
        self.in_menu = False
        self.in_game = True

        self.answer_nonogram = np.zeros((size_of_nonogram, size_of_nonogram), dtype=int)

        self.clearwin()

        self.canvas = Canvas(self.window, width=size_of_canvas, height=size_of_canvas, background=background_colour)
        self.canvas.pack()

        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

        self.window.bind('<Return>', self.end_game)

        self.initialize_nonogram()
        self.puzzle_info(nonogram)
        self.win = False
        self.exit = False
        self.game_finished = False


    def clearwin(self):
        #Clear the main windows frame of all widgets
        for child in self.window.winfo_children():
            child.destroy()

    def mainloop(self):
        self.window.mainloop()

    def initialize_nonogram(self):
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid + size_of_outskirts, 0, i * size_of_grid + size_of_outskirts,
                                    size_of_board + size_of_outskirts, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid + size_of_outskirts, size_of_board + size_of_outskirts,
                                    i * size_of_grid + size_of_outskirts, width = 2)



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

    def change_grid_status(self, click_position):

        #treating left upper corner like coords 0,0
        click_position[0]-=size_of_outskirts
        click_position[1]-=size_of_outskirts

        # Check if the click was outside board
        if click_position[0] < 0 or click_position[1] < 0:
            return
        if click_position[0] > size_of_board or click_position[1] > size_of_board:
            return

        for i in range(size_of_nonogram + 1):
            if click_position[0] <= i * size_of_grid and click_position[0] >= (i - 1) * size_of_grid:
                x_position = (i - 1) * size_of_grid + size_of_outskirts
                col = i - 1
                break
        for i in range(size_of_nonogram + 1):
            if click_position[1] <= i * size_of_grid and click_position[1] >= (i - 1) * size_of_grid:
                y_position = (i - 1) * size_of_grid + size_of_outskirts
                row = i - 1
                break
        if self.answer_nonogram[row][col] == 0:
            self.answer_nonogram[row][col] = 1
            self.canvas.create_rectangle(x_position, y_position, x_position + size_of_grid, y_position + size_of_grid, fill = marked_grid_colour)
        else:
            self.answer_nonogram[row][col] = 0
            self.canvas.create_rectangle(x_position,y_position,x_position + size_of_grid,y_position + size_of_grid, fill = background_colour)

    def check_win(self):
        if (self.nonogram == self.answer_nonogram).all():
            return True

        return False

    def end_game(self,event):
        if self.win == True:
            self.in_game = False
            self.canvas.delete("all")
            self.print_nonogram()
            self.game_finished = True
            self.win = False
            return
        if self.game_finished == True:
            self.clearwin()
            self.main_menu()


    def print_nonogram(self):
        for i in range(size_of_nonogram):
            for j in range(size_of_nonogram):
                if self.nonogram[i][j] == 1:
                    self.canvas.create_rectangle(j * size_of_nonogram * 2, i * size_of_nonogram * 2, (j + 1) * size_of_nonogram * 2,
                                                 (i + 1) * size_of_nonogram * 2, fill=marked_grid_colour)
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid, 0, i * size_of_grid, size_of_board, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid, size_of_board, i * size_of_grid, width = 2)

    def click(self, event):
        if self.in_game == True:
            click_position = [event.x, event.y]
            self.change_grid_status(click_position)
            self.win = self.check_win()
            self.initialize_nonogram()#used to keep thick lines
            if self.win == True:
                self.canvas.create_text(size_of_outskirts / 2,size_of_outskirts / 2, text = "Wygrałeś!", font="Times 20")
                self.canvas.create_text(size_of_outskirts / 2, size_of_outskirts / 2 + 20,
                 text="Naciśnij enter aby kontynuować", font="Times 10")







game_instance = Nonogram()
game_instance.mainloop()