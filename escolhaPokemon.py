from tkinter import *
from tkinter import messagebox
import random


def btnSquirtleClick():
    messagebox.showinfo('Pokemons', 'Boa escolha!')
    quit()


def btnCharmanderClick():
    messagebox.showinfo('Pokemons', 'Péssima escolha!')
    quit()


def motionMouse(event):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    btnCharmander.place(x=x, y=y)


def btnBulbasaurClick():
    messagebox.showinfo('Pokemons', 'Boa escolha!')
    quit()


root = Tk()
root.title("Pokemons")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="white")

label = Label(root, text="Qual o melhor Pokemon inicial?",
              font=("Arial", 20, "bold"))
label.place(x=140, y=50)

btnSquirtle = Button(root, text="Squirtle", font=(
    "Arial", 20, "bold"), command=btnSquirtleClick)
btnSquirtle.place(x=50, y=100)

btnCharmander = Button(root, text="Charmander", font=("Arial", 20, "bold"))
btnCharmander.place(x=180, y=100)
btnCharmander.bind("<Enter>", motionMouse)
btnCharmander.config(command=btnCharmanderClick)

btnBulbasaur = Button(root, text="Bulbassauro", font=(
    "Arial", 20, "bold"), command=btnBulbasaurClick)
btnBulbasaur.place(x=340, y=100)

root.mainloop()
