
#NIE SKONCZONE
#123

from tkinter import *
import numpy as np

size_of_nonogram = 15
size_of_grid = 30
size_of_board = size_of_nonogram*size_of_grid
size_of_canvas = 700
size_of_outskirts = 6 * size_of_grid
size_of_font = 30
result_matrix = None

answer_nonogram = np.zeros((size_of_nonogram,size_of_nonogram),dtype=int)
marked_grid_colour = '#444444'
background_colour = '#F5F5F5'


class Nonogram():
    # Initialization functions
    def __init__(self):
        self.window = Tk()
        self.window.title('Nonogram')
        self.canvas = Canvas(self.window, width=size_of_canvas, height=size_of_canvas, background = background_colour)
        self.canvas.pack()
        self.end_button()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)


        self.initialize_nonogram()
        # self.puzzle_info(nonogram)  #TODO zmienic tak, by przy kliknieciu pojawiala sie cyfra



    # Tkinter event loop
    def mainloop(self):
        self.window.mainloop()

    # drawing lines
    def initialize_nonogram(self):
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid + size_of_outskirts, 0, i * size_of_grid + size_of_outskirts, size_of_board + size_of_outskirts, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid + size_of_outskirts, size_of_board + size_of_outskirts, i * size_of_grid + size_of_outskirts, width = 2)

    # Printing end_button
    def end_button(self):

        button1 = Button(self.window, text="END", command=(lambda: self.end_game()))  # lambda dodana, bo jak przekazuje funkcje to przycisk automatycznie się odpala
        button1.pack()

    #TODO do zmienienia, tak, ze jak gracz kliknie to pojawia się cyferka
    # def puzzle_info(self,nonogram):#TODO Optimalization of this function
    #     #columns
    #     ones_counter = 0
    #     columns = list(zip(*nonogram))
    #     array = []
    #     for i in range(size_of_nonogram):
    #         for j in range(size_of_nonogram):
    #             if not ones_counter - 1 == 0 and ones_counter > 0:
    #                 ones_counter -= 1
    #                 continue
    #             ones_counter = 0
    #             first_one = columns[i][j]
    #             if first_one == 1:
    #                 ones_counter = 1
    #                 for z in range(j+1,size_of_nonogram):
    #                     if columns[i][z] == 0:
    #                         break
    #                     else:
    #                         ones_counter+=1
    #             if not ones_counter == 0:
    #                 array.append(ones_counter)
    #         if not array == []:
    #             for j in range(len(array)):
    #                 self.canvas.create_text(size_of_outskirts+size_of_grid / 2 + size_of_grid * i,
    #                                         (j + 1) * size_of_font,font="Times 20",text = str(array[j]))
    #         array.clear()
    #     #rows
    #     ones_counter = 0
    #     rows = nonogram
    #     array = []
    #     for i in range(size_of_nonogram):
    #         for j in range(size_of_nonogram):
    #             if not ones_counter - 1 == 0 and ones_counter > 0:
    #                 ones_counter -= 1
    #                 continue
    #             ones_counter = 0
    #             first_one = rows[i][j]
    #             if first_one == 1:
    #                 ones_counter = 1
    #                 for z in range(j + 1, size_of_nonogram):
    #                     if rows[i][z] == 0:
    #                         break
    #                     else:
    #                         ones_counter += 1
    #             if not ones_counter == 0:
    #                 array.append(ones_counter)
    #         if not array == []:
    #             for j in range(len(array)):
    #                 self.canvas.create_text((j + 1) * size_of_font,size_of_outskirts + size_of_grid / 2 + size_of_grid * i,
    #                                         font="Times 20", text=str(array[j]))
    #         array.clear()

    def change_grid_status(self, click_position):

        # treating left upper corner like coords 0,0
        # TODO dlaczego?
        click_position[0] -= size_of_outskirts  # event x
        click_position[1] -= size_of_outskirts  # event y

        # End game
        if click_position[0] < 0 and click_position[1] < 0:
            if click_position[0] > -(3 * size_of_grid) and click_position[1]> -(2 * size_of_grid):
                print("win")
                self.win = True


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

        # wypełninie kratek
        if answer_nonogram[row][col] == 0:
            answer_nonogram[row][col] = 1
            self.canvas.create_rectangle(x_position, y_position, x_position + size_of_grid, y_position + size_of_grid, fill = marked_grid_colour)
        else:
            answer_nonogram[row][col] = 0
            self.canvas.create_rectangle(x_position,y_position,x_position + size_of_grid,y_position + size_of_grid, fill = background_colour)

    def end_game(self):
        print("win")
        end_result = answer_nonogram
        self.window.destroy()
        return end_result

    def click(self, event):
        click_position = [event.x, event.y]
        self.change_grid_status(click_position)

        self.initialize_nonogram()  # used to keep thick lines





game_instance = Nonogram()
game_instance.mainloop()
