from tkinter import *
import numpy as np
import save_and_load as sv

size_of_nonogram = 15
size_of_grid = 30
size_of_board = size_of_nonogram*size_of_grid
size_of_canvas = 700
size_of_outskirts = 6 * size_of_grid
size_of_font = 30

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
        #przycisk zamykający okno tkintera
        self.end_button()
        # Input from user in form of clicks
        self.window.bind('<Button-1>', self.click)


        self.initialize_nonogram()

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

        button1 = Button(self.window, text="END", command=(lambda: self.end_game()))  # lambda dodana, bo jak przekazuje tylko funkcje to przycisk automatycznie się odpala
        button1.pack()

    def change_grid_status(self, click_position):

        # treating left upper corner like coords 0,0
        click_position[0] -= size_of_outskirts  # event x
        click_position[1] -= size_of_outskirts  # event y



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
        sv.save_as_file(answer_nonogram, 'Stworzone_z_gui.pkl', 'Stworzone_z_gui.pkl')
        name_picture = text_box()
        name_picture.mainloop()
        self.window.destroy()


    def click(self, event):
        click_position = [event.x, event.y]
        self.change_grid_status(click_position)

        self.initialize_nonogram()  # used to keep thick lines

class text_box(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.entry = Entry(self)
        self.button = Button(self, text="Zapisz i wyjdź", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        l = sv.load_list_from_file('Stworzone_z_gui.pkl')
        n = len(l)
        sv.rename(n-1, self.entry.get(), 'Stworzone_z_gui.pkl')
        self.destroy()



game_instance = Nonogram()
game_instance.mainloop()
