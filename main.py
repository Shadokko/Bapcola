# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import Canvas


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Salut, {name} !')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Bapcola')

    from tkinter import *
    from PIL import Image, ImageTk
    from pathlib2 import Path
    from bapcola_package import utils

    # initializing parameters
    utils.parse_yaml('parameters.yml')

    fenetre = Tk()

    label = Label(fenetre, text="MON JEU PACMAN")
    label.pack()

    canvas = Canvas(fenetre, width=canvas_width, height=canvas_heigth, background='blue')

    path2image = Path('C:/Users/nfaur/Documents/Bapcola') / 'Pacman.png'
    mon_image =  Image.open(str(path2image)).resize((100,100))
    mon_image_tk = ImageTk.PhotoImage(mon_image)
    canvas.create_image(canvas_width // 2,canvas_heigth // 2, image=mon_image_tk)
    canvas.pack()

    fenetre.mainloop()
