# 1 is coding black instead of white, there's two functionalities: switching colours between white and black and program autochecking
#corretnes of solution but doesn't show numbers of grids in each columns/rows
from tkinter import *
import numpy as np

size_of_nonogram = 15
size_of_grid = 30
size_of_board = size_of_nonogram*size_of_grid
size_of_canvas = 600

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
          [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1]]#sample from polish wikipedia from 'methods of solving' section
'''nonogram=[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]'''
answer_nonogram = np.zeros((15,15),dtype=int)
marked_grid_colour = '#444444'
background_colour = '#F5F5F5'


class Nonogram():
    #Initialization functions
    def __init__(self):
        self.window = Tk()
        self.window.title('Nonogram')
        self.canvas = Canvas(self.window, width=size_of_canvas, height=size_of_canvas, background = background_colour)
        self.canvas.pack()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)

        self.initialize_nonogram()
        self.gameover = False
        self.win = False

    def mainloop(self):
        self.window.mainloop()

    def initialize_nonogram(self):
        for i in range(size_of_nonogram):
            self.canvas.create_line((i + 1) * size_of_grid, 0, (i + 1) * size_of_grid, size_of_board, width = 2)

        for i in range(size_of_nonogram):
            self.canvas.create_line(0, (i + 1) * size_of_grid, size_of_board, (i + 1) * size_of_grid, width = 2)


    #Drawing and logical functions


    def change_grid_status(self, click_position):
        #TODO
        #Check if the click was outside board to avoid errors

        for i in range(size_of_nonogram + 1):
            if click_position[0] <= i * size_of_grid and click_position[0] >= (i - 1) * size_of_grid:
                x_position = (i - 1) * size_of_grid
                col = i - 1
                break
        for i in range(size_of_nonogram + 1):
            if click_position[1] <= i * size_of_grid and click_position[1] >= (i - 1) * size_of_grid:
                y_position = (i - 1) * size_of_grid
                row = i - 1
                break
        if answer_nonogram[row][col] == 0:
            answer_nonogram[row][col] = 1
            self.canvas.create_rectangle(x_position, y_position, x_position + size_of_grid, y_position + size_of_grid, fill = marked_grid_colour)
        else:
            answer_nonogram[row][col] = 0
            self.canvas.create_rectangle(x_position,y_position,x_position + size_of_grid,y_position + size_of_grid, fill = background_colour)

    def check_win(self):
        if (nonogram == answer_nonogram).all():
            print("win")
            return True

        return False

    def click(self, event):
        click_position = [event.x, event.y]
        self.change_grid_status(click_position)
        self.initialize_nonogram()#used to keep thick lines
        self.check_win()




game_instance = Nonogram()
game_instance.mainloop()
