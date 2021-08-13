import tkinter as tk
window = tk.Tk()

f = tk.Frame(bg = "light gray")
f.pack ()

maingarden = tk.PhotoImage(file = "Garden1.png")
a = tk.Label(master = window, image = maingarden)
a.pack (side=tk.BOTTOM)

lblone = tk.Label (master = f, text = "- Botanical Garden Search Engine -", width = 42, height = 2, font = ("Arial", 15))
lblone.pack()
lbltwo = tk.Label (master = f, text = "Search in this collection to get info on certain plants and trees including:\n 1. Roses\n 2. Cacti\n 3. Palm Trees\n 4. Azaleas\n 5. Maple Trees", width = 58, height = 6, font = ("Arial, 10"))
lbltwo.pack()

ftwo = tk.Frame (bg = "light Gray")
ftwo.pack ()

entone = tk.Entry (master = ftwo, width = 58, font = ("Arial", 10), bg = "white", fg = "black")
entone.pack(side = tk.LEFT)
butone = tk.Button (master = ftwo, bg = "gray", fg = "black", text = "Enter")
butone.pack(side = tk.LEFT)

def displayPic (event):
    text = entone.get()
    entone.delete (0, tk.END)
    a.pack_forget ()
    fthree = tk.Frame (bg = "light gray")
    fthree.pack ()
    if text == "1":
        lblrose = tk.Label (master = fthree, width = 58, height = 7, font = ("Arial", 10), text = "- Roses -\nRoses are part of a plant family that can produce flowers that can\nbloom in a variety of colors. Roses have been domesticated since\na long time ago. Usually, roses contain petals that can bloom only\nduring the spring, though so gentically modified roses could easily\nfix the problem. Roses also have thorns so be careful!")
        lblrose.pack()
        butrose = tk.Button (master = fthree, bg = "gray", fg = "black", text = "Close Information")
        butrose.pack()
        def displayRose (event):
            lblrose.pack_forget ()
            butrose.pack_forget ()
            fthree.pack_forget ()
        butrose.bind ("<Button-1>", displayRose)
    elif text == "2":
        lblcac = tk.Label (master = fthree, width = 58, height = 7, font = ("Arial", 10), text = "- Cacti -\nCacti are part of the plant family Cactaceae and are most commonly\nfound in deserts all around the world. Cacti have spikes on their\nbody to prevent being eaten by predators. Cacti have water stored\ninsides, and some cacti even have flowers on their body, too. Some\nanimals have techniques to obtain water from cacti without getting hurt.")
        lblcac.pack()
        butcac = tk.Button (master = fthree, bg = "gray", fg = "black", text = "Close Information")
        butcac.pack()
        def displayCac (event):
            lblcac.pack_forget ()
            butcac.pack_forget ()
            fthree.pack_forget ()
        butcac.bind ("<Button-1>", displayCac)
    elif text == "3":
        lblpal = tk.Label (master = fthree, width = 58, height = 7, font = ("Arial", 10), text = "- Palm Trees -\nPalm Trees are actually Arecaceae that are shaped like a tree. Palm\nTrees are usually found in tropical and in subtropical climates. Palm\nTrees also can produce a variety of coconuts depending on the type\nof Palm Tree and grow in various different soils. Palm Trees from the\nWest Coast of the US can produce about 80 coconuts every year.")
        lblpal.pack()
        butpal = tk.Button (master = fthree, bg = "gray", fg = "black", text = "Close Information")
        butpal.pack()
        def displayPal (event):
            lblpal.pack_forget ()
            butpal.pack_forget ()
            fthree.pack_forget ()
        butpal.bind ("<Button-1>", displayPal)
    elif text == "4":
        lblaza = tk.Label (master = fthree, width = 58, height = 7, font = ("Arial", 10), text = "- Azaleas -\nAzaleas are shrubs with flowers that bloom during the springtime.\nDue to selective breeding, azaleas come in a variety of colors and\nare fairly shade tolerant. Azaleas are part of the plant family Er-\nicaceae and prefer living near or under trees. Azaleas are slightly\npoisonous and carries toxins within its nectar and its leaves.")
        lblaza.pack()
        butaza = tk.Button (master = fthree, bg = "gray", fg = "black", text = "Close Information")
        butaza.pack()
        def displayAza (event):
            lblaza.pack_forget ()
            butaza.pack_forget ()
            fthree.pack_forget ()
        butaza.bind ("<Button-1>", displayAza)
    elif text == "5":
        lblmap = tk.Label (master = fthree, width = 58, height = 7, font = ("Arial", 10), text = "- Maple Trees -\nMaple Trees are part of the plant family of Sapindaceae and can grow\nmainly in the Northern Hemisphere. There are about 132 variations of\nMaple Trees and some of the species can produce an edible sap. Most\nMaple Trees have the potential to grow over 140 feet tall, and has leaves\nthat turn orange during the autumn season.")
        lblmap.pack()
        butmap = tk.Button (master = fthree, bg = "gray", fg = "black", text = "Close Information")
        butmap.pack()
        def displayMap (event):
            lblmap.pack_forget ()
            butmap.pack_forget ()
            fthree.pack_forget ()
        butmap.bind ("<Button-1>", displayMap)
    else:
        lblcor = tk.Label (master = fthree, width = 58, height = 2, font = ("Arial", 10), text = "Please just type in the number, not the words.")
        lblcor.pack ()
        butcor = tk.Button (master = fthree, bg = "gray", fg = "black", text = "Close Information")
        butcor.pack ()
        def displayCor (event):
            lblcor.pack_forget ()
            butcor.pack_forget ()
            fthree.pack_forget ()
        butcor.bind ("<Button-1>", displayCor)
butone.bind ("<Button-1>", displayPic)
window.mainloop()