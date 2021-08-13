score = 0
arrow = 0
hit = 0
award = ""
lights = []
cac = False
shiny = False

import tkinter as tk
from types import prepare_class
window = tk.Tk ()

c = tk.Canvas (bg = "light blue", height = 600, width = 500)
c.pack()

bullseye = tk.PhotoImage (file = "Bullseye1.png")
plus = tk.PhotoImage (file = "Plus1.png")
firearrow = tk.PhotoImage (file = "FireArrow.png")

mouseX = -1
mouseY = -1

def update ():
    c.create_rectangle(0, 0, 600, 500, fill="light blue", outline="light blue") # draw background

    c.create_rectangle (0,0,502,40, fill = "light gray", outline = "light gray")
    c.create_text (250,20, text = "The Archery Game", fill = "black", font = ("Cambria", 18))
    c.create_rectangle (0,570,502,600, fill = "light gray", outline = "light gray")
    c.create_text (100, 585, text = "Use Curser to Aim", fill = "black", font = ("Cambria", 10))
    c.create_rectangle (420, 570, 502, 600, fill = "gray", outline = "gray")
    c.create_text (460,585, text = "Medal", fill = "black", font = ("Cambria", 10))
    c.create_rectangle (420, 0, 502, 40, fill = "gray", outline = "gray")
    c.create_text (460, 20, text = "Reset", fill = "black", font = ("Cambria", 10))
    c.create_oval (220, 580, 230, 590, fill = "gray")
    c.create_oval (260, 580, 270, 590, fill = "gray")
    c.create_oval (300, 580, 310, 590, fill = "gray")
    c.create_rectangle (0,350,50,570, fill = "green", outline = "green")
    c.create_rectangle (50,350,100,570, fill = "light green", outline = "light green")
    c.create_rectangle (100,350,150,570, fill = "green", outline = "green")
    c.create_rectangle (150,350,200,570, fill = "light green", outline = "light green")
    c.create_rectangle (200,350,250,570, fill = "green", outline = "green")
    c.create_rectangle (250,350,300,570, fill = "light green", outline = "light green")
    c.create_rectangle (300,350,350,570, fill = "green", outline = "green")
    c.create_rectangle (350,350,400,570, fill = "light green", outline = "light green")
    c.create_rectangle (400,350,450,570, fill = "green", outline = "green")
    c.create_rectangle (450,350,500,570, fill = "light green", outline = "light green")
    c.create_rectangle (500,350,550,570, fill = "light green", outline = "light green")
    c.create_rectangle (0,300,500,350, fill = "blue", outline = "blue")
    c.create_oval (100, 50, 150, 100, fill = "white", outline = "white")
    c.create_oval (125, 50, 175, 100, fill = "white", outline = "white")
    c.create_oval (150, 50, 200, 100, fill = "white", outline = "white")
    c.create_oval (175, 50, 225, 100, fill = "white", outline = "white")
    c.create_oval (300, 100, 350, 150, fill = "white", outline = "white")
    c.create_oval (325, 100, 375, 150, fill = "white", outline = "white")
    c.create_oval (350, 100, 400, 150, fill = "white", outline = "white")
    c.create_oval (375, 100, 425, 150, fill = "white", outline = "white")
    c.create_rectangle (245, 300, 255, 380, fill = "brown", outline = "brown")
    c.create_image (250, 300, image = bullseye)
    c.create_rectangle (40, 300, 60, 375, fill = "brown", outline = "brown")
    c.create_rectangle (130, 300, 150, 375, fill = "brown", outline = "brown")
    c.create_rectangle (440, 300, 460, 375, fill = "brown", outline = "brown")
    c.create_rectangle (350, 300, 370, 375, fill = "brown", outline = "brown")
    c.create_polygon (360, 100, 330, 330, 390, 330, fill = "green")
    c.create_polygon (450, 100, 420, 330, 480, 330, fill = "green")
    c.create_polygon (140, 100, 110, 330, 170, 330, fill = "green")
    c.create_polygon (50, 100, 20, 330, 80, 330, fill = "green")
    
    c.create_image(mouseX, mouseY, image = plus)

    global hit, cac
    if hit >= 1:
        c.create_image (250, 300, image = firearrow)
        if hit >= 2:
            c.create_image (230, 350, image = firearrow)
            if hit >= 3:
                c.create_image (270, 350, image = firearrow)
    if cac == True:
        c.create_oval (220, 580, 230, 590, fill = "gray")
        c.create_oval (260, 580, 270, 590, fill = "gray")
        c.create_oval (300, 580, 310, 590, fill = "gray")

    if len(lights) >= 1:
        c.create_oval (220, 580, 230, 590, fill = lights[0])
        if len(lights) >= 2:
            c.create_oval (260, 580, 270, 590, fill = lights[1])
            if len(lights) >= 3:
                c.create_oval (300, 580, 310, 590, fill = lights[2])
    
    global shiny
    if shiny == True:
        global award
        if award == "gold":
            c.create_oval (440, 510, 480, 550, fill = "gold")
            c.create_text (460, 530, text = "Gold")
        elif award == "silver":
            c.create_oval (440, 510, 480, 550, fill = "silver")
            c.create_text (460, 530, text = "Silver")
        elif award == "bronze":
            c.create_oval (440, 510, 480, 550, fill = "brown")
            c.create_text (460, 530, text = "Bronze")
        elif award == "nothing":
            c.create_text (460, 530, text = "You didn't get\nan award :(")

    window.after(50,update)
window.after (0, update)

def movement (event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
c.bind ("<Motion>", movement)

def fire (event):
    global hit, arrow, score
    arrow = arrow+1
    if score < 3:
        if mouseX >= 210 and mouseX <= 290 and mouseY >= 255 and mouseY <= 330:
            lights.append ("green")
            hit = hit + 1
        else:
            lights.append ("red")
        score = score+1

def reset (event):
    global hit, arrow, score, cac, award, lights
    if mouseX >= 420 and mouseX <= 502 and mouseY >= 0 and mouseY <= 40:
        score = 0
        hit = 0
        arrow = 0
        cac = True
        award = ""
        lights = []

def medal (event):
    global award, shiny
    if mouseX >= 420 and mouseX <= 502 and mouseY >= 570 and mouseY <= 600:
        shiny = True
        if score == 3 and hit == 0:
            award = "nothing"
        elif score == 3 and hit == 1:
            award = "bronze"
        elif score == 3 and hit == 2:
            award = "silver"
        elif score == 3 and hit == 3:
            award = "gold"

def onClick(event):
    fire(event)
    reset(event)
    medal(event)
c.bind ("<Button-1>", onClick)



window.mainloop ()