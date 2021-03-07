
# importing packages
import tkinter
import ruamel.yaml as yaml
from bapcola_package import utils, classes

if __name__ == '__main__':

    # parsing parameters
    path2yaml = 'parameters.yml'
    yaml_file = open(path2yaml, 'r')
    yaml_content = yaml.load(yaml_file, Loader=yaml.Loader)
    print("Key: Value")
    for key, value in yaml_content.items():
        print(f"{key}: {value}")
        if type(value) is str:
            exec('{} = "{}"'.format(key, value))
        else:
            exec('{} = {}'.format(key, value))

    fenetre = tkinter.Tk()

    label = tkinter.Label(fenetre, text="MON JEU PACMAN")
    label.pack()

    canvas = tkinter.Canvas(fenetre, width=canvas_width, height=canvas_heigth, background='blue')

    # On crée l'object pacman
    pacman = classes.pacman(canvas, path2data, position=(canvas_width // 2, canvas_heigth // 2))

    # On passe les saisies clavier vers l'object Pacman
    canvas.focus_set()
    # canvas.bind("<Key>", pacman.print_input_key)
    canvas.bind("<Key>", pacman.behavior_on_key)

    canvas.pack()

    fenetre.mainloop()
