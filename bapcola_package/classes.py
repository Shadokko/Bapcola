from pathlib2 import Path
from PIL import Image, ImageTk
import tkinter as tk
import time

class pacman():
    """
    La classe PACMAN

    Définit les attributs de PACMAN

    - position
    - orientation
    - taille

    Définit les méthodes de PACMAN
    - se déplacer

    """
    def __init__(self, canvas, path2data,
                 position=(10, 10)):
        self.canvas = canvas
        self.position = position
        self.path2data = path2data
        path2image = Path(path2data) / 'Pacman.png'
        mon_image = Image.open(str(path2image)).resize((100, 100))
        self.appearance = ImageTk.PhotoImage(mon_image)
        self.img_id = None
        self.update_image()

    def print_input_key(self, event):
        touche = event.keysym
        print(touche)

    def behavior_on_key(self, event):
        key = event.keysym

        if key == 'Right':
            self.position = (self.position[0] + 10, self.position[1])
            self.update_image()

        if key == "Left":
            self.position = (self.position[0] - 10, self.position[1])
            self.update_image()

        if key == "Up":
            self.position = (self.position[0], self.position[1] - 10)
            self.update_image()

        if key == "Down":
            self.position = (self.position[0], self.position[1] + 10)
            self.update_image()

    def update_image(self):
        if self.img_id is not None:
            self.canvas.delete(self.img_id)
        self.img_id = self.canvas.create_image(self.position[0],
                                               self.position[1],
                                               image=self.appearance)












