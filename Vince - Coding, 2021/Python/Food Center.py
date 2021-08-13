import os
import tkinter as tk
window = tk.Tk()

f = tk.Frame(bg = "light gray")
f.pack ()

lblone = tk.Label (master = f, text = "= Food Center =", width = 28, height = 1, bg = "green", fg = "gold", font = ("Cambria", 23))
lblone.pack ()
lbltwo = tk.Label (master = f, text = "\nClick buttons in the food center to access windows\non certain types of food and information about them.\n", width = 50, height = 4, bg = "light gray", fg = "black", font = ("Cambria", 11))
lbltwo.pack ()

food = tk.PhotoImage (file = "CentralFood1.png")
a = tk.Label (master = window, image = food)
a.pack (side = tk.TOP)

ftwo = tk.Frame(bg = "light gray")
ftwo.pack ()

lblthree = tk.Label (master = ftwo, text = "\n- Food Options -\nSelect your type of food that you want to learn\nimportant information about (click the buttons).\n", width = 59, height = 5, bg = "light gray", fg = "black", font = ("Cambria", 11))
lblthree.pack ()

ff = tk.Frame(bg = "light gray")
ff.pack ()

butus = tk.Button (master = ff, bg = "gray", fg = "black", width = 33, text = "American")
butus.pack(side = tk.LEFT)
def displayOne (event):
    os.system ("python \"American Foods.py\"")
butjapan = tk.Button (master = ff, bg = "gray", fg = "black", width = 33, text = "Japanese")
butjapan.pack(side = tk.RIGHT)
def displayTwo (event):
    os.system ("python \"Japanese Cuisine.py\"")

fthree = tk.Frame(bg = "light gray")
fthree.pack ()

butitalian = tk.Button (master = fthree, bg = "gray", fg = "black", width = 33, text = "Italian")
butitalian.pack(side = tk.LEFT)
def displayThree (event):
    os.system ("python \"Italian Food.py\"")
butfrench = tk.Button (master = fthree, bg = "gray", fg = "black", width = 33, text = "French")
butfrench.pack(side = tk.RIGHT)
def displayFour (event):
    os.system ("python \"French Cuisine.py\"")

butus.bind ("<Button-1>", displayOne)
butjapan.bind ("<Button-1>", displayTwo)
butitalian.bind ("<Button-1>", displayThree)
butfrench.bind ("<Button-1>", displayFour)

window.mainloop ()