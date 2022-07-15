score = 0

import tkinter as tk
from types import prepare_class
window = tk.Tk ()

c = tk.Canvas (bg = "light gray", height = 600, width = 600)
c.pack()

#star = tk.PhotoImage (file = ".png")
capb = tk.PhotoImage (file = "Capitol Building.jpg")

c.create_polygon (0,0,40,0,0,75, fill = "white")
c.create_polygon (0,75,40,0,80,0,0,150, fill = "#d90000")
c.create_polygon (0,150,80,0,120,0,0,225, fill = "white")
c.create_polygon (0,225,120,0,160,0,0,300, fill = "#d90000")
c.create_polygon (0,0,160,0,120,75,0,75, fill = "#2F2269")
c.create_polygon (600,600,600,525,560,600, fill = "white")
c.create_polygon (600,525,600,450,520,600,560,600, fill = "#d90000")
c.create_polygon (600,450,600,375,480,600,520,600, fill = "white")
c.create_polygon (600,375,600,300,440,600,480,600, fill = "#d90000")
c.create_polygon (600,600,600,525,480,525,440,600, fill = "#2F2269")
#c.create_image (250, 300, image = star)

c.create_text (300,100, text = "Political Quiz", fill = "black", font = ("Cambria", 39))
c.create_text (320,225, text = "Hello! Welcome to the Political Quiz! In this game,\nyou will be given questions on a variety of topics,\nand in the end, the game will determine your political\nparty and match your political identity to someone in\nthe U.S. government. Please note that this political\nquiz does not endorse any government official and\nexists for entertainment purposes only.", fill = "black", font = ("Cambria",13))
c.create_image (300,450, image = capb)

window.mainloop ()