
from tkinter import *
import numpy as np

size_of_nonogram = 15 #lenght of nonograms rows/columns
size_of_grid = 30 #distance between lines in pixels 
size_of_board = size_of_nonogram*size_of_grid
size_of_canvas = 700 #size of window
size_of_outskirts = 6 * size_of_grid #distance from window border to board
size_of_font = 30

'''nonogram=[[1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
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
          [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1]]#example from polish wikipedia from 'methods of solving' section'''
nonogram=[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
answer_nonogram = np.zeros((size_of_nonogram,size_of_nonogram),dtype=int)
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

        self.window.bind('<Return>', self.end_game)

        self.initialize_nonogram()
        self.puzzle_info(nonogram)
        self.win = False
        self.exit = False

    def mainloop(self):
        self.window.mainloop()

    def initialize_nonogram(self):#function is creating all lines
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid + size_of_outskirts, 0, i * size_of_grid + size_of_outskirts,
                                    size_of_board + size_of_outskirts, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid + size_of_outskirts, size_of_board + size_of_outskirts,
                                    i * size_of_grid + size_of_outskirts, width = 2)


    #Drawing and logical functions
                                   #TODO Optimalization of this function
    def puzzle_info(self,nonogram):#Function takes a nonogram and then calculates the numbers that should help the user solve the puzzle, and then writes them
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

    def change_grid_status(self, click_position):#Function takes click position (x and y coordinates) checks if the click was inside board calculates square coordinates
                                                 #then changing answer nonogram and colour of proper square
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
        if answer_nonogram[row][col] == 0:
            answer_nonogram[row][col] = 1
            self.canvas.create_rectangle(x_position, y_position, x_position + size_of_grid, y_position + size_of_grid, fill = marked_grid_colour)
        else:
            answer_nonogram[row][col] = 0
            self.canvas.create_rectangle(x_position,y_position,x_position + size_of_grid,y_position + size_of_grid, fill = background_colour)

    def check_win(self):#Function is checking equality between answer nonogram and solved one
        if (nonogram == answer_nonogram).all():
            print("win")
            return True

        return False

    def end_game(self,event):#Function clears window and runnnig print_nonogram function
        if self.win == True:
            self.canvas.delete("all")
            self.print_nonogram()


    def print_nonogram(self):#Function is writing solved nonogram
        for i in range(size_of_nonogram):
            for j in range(size_of_nonogram):
                if nonogram[i][j] == 1:
                    self.canvas.create_rectangle(j * size_of_nonogram * 2, i * size_of_nonogram * 2, (j + 1) * size_of_nonogram * 2,
                                                 (i + 1) * size_of_nonogram * 2, fill=marked_grid_colour)
        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(i * size_of_grid, 0, i * size_of_grid, size_of_board, width = 2)

        for i in range(size_of_nonogram + 1):
            self.canvas.create_line(0, i * size_of_grid, size_of_board, i * size_of_grid, width = 2)

    def click(self, event):#Function realizing all operations that should be done after users click
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
