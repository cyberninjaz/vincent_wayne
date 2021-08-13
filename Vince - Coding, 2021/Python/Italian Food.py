import tkinter as tk
window = tk.Tk ()

f = tk.Frame (bg = "light gray")
f.pack ()

lblone = tk.Label (master = f, text = "- Italian Food -", bg = "green", fg = "red", width = 28, font = ("Cambria", 24))
lblone.pack ()
lbltwo = tk.Label (master = f, bg = "light gray", font = ("Cambria", 11), height = 4, width = 64, text = "\nSearch in the window to find notable Italian Foods in the United States. This\nis not a restaurant website for browsing food or a website for purchasing food.\n")
lbltwo.pack ()

pasta = tk.PhotoImage (file = "Italian Food1.png")
a = tk.Label (master = window, image = pasta)
a.pack (side = tk.TOP)

ftwo = tk.Frame (bg = "light gray")
ftwo.pack ()

lblthree = tk.Label (master = ftwo, bg = "light gray", text = "- Foods -", font = ("Cambria", 11), width = 64)
lblthree.pack ()

fthree = tk.Frame (bg = "light gray")
fthree.pack ()

butone = tk.Button (master = fthree, bg = "gray", fg = "black", width = 31, font = ("Cambria", 11),text = "Spaghetti")
butone.pack(side = tk.LEFT)
def displayOne (event):
    fsp = tk.Frame (bg = "light gray")
    fsp.pack ()
    lblspone = tk.Label (master = fsp, height = 1, font = ("Cambria", 20), fg = "red", bg = "green", width = 34, text = "- Spaghetti -")
    lblspone.pack ()
    lblsptwo = tk.Label (master = fsp, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Italian Spaghetti is simply long, thin strips of boiled dough put on a plate.\nSpaghetti can come in many variations, though spaghetti usually is covered\nwith a tomato meat sauce along with a sprinkle of cheese (the sprinkled cheese\nis normally parmesan). Sometimes spaghetti is covered simply in olive oil\nthough in reality. You can cover it with anything. Now, spaghetti comes\nin boxes, so you don't have to go through the long, tedious process.")
    lblsptwo.pack ()
    butsp = tk.Button (master = fsp, width = 72, bg = "gray", fg = "black", text = "Close Information")
    butsp.pack ()
    def displaySp (event):
        fsp.pack_forget ()
    butsp.bind ("<Button-1>", displaySp)
buttwo = tk.Button (master = fthree, bg = "gray", fg = "black", width = 31, font = ("Cambria", 11),text = "Focaccia")
buttwo.pack(side = tk.RIGHT)
def displayTwo (event):
    ffo = tk.Frame (bg = "light gray")
    ffo.pack ()
    lblfoone = tk.Label (master = ffo, height = 1, font = ("Cambria", 20), fg = "red", bg = "green", width = 34, text = "- Focaccia -")
    lblfoone.pack ()
    lblfotwo = tk.Label (master = ffo, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Focaccia is Italian bread baked in the oven that is relatively flat. Focaccia\nis usually served as a side dish to accompany larger Italian dishes, though\nit tastes just as good by itself. Focaccia normally has herbs imbeded inside\nitself including basil and rosemary. Focaccia can also be used as a bread\nfor sandwiches due to it having a strong, yet fluffy consitency. Focaccia\nis now made all around the world and can be found in tons of restaurants.")
    lblfotwo.pack ()
    butfo = tk.Button (master = ffo, width = 72, bg = "gray", fg = "black", text = "Close Information")
    butfo.pack ()
    def displayFo (event):
        ffo.pack_forget ()
    butfo.bind ("<Button-1>", displayFo)

ffour = tk.Frame (bg = "light gray")
ffour.pack ()

butthree = tk.Button (master = ffour, bg = "gray", fg = "black", width = 31, font = ("Cambria", 11),text = "Cannolis")
butthree.pack(side = tk.LEFT)
def displayThree (event):
    fca = tk.Frame (bg = "light gray")
    fca.pack ()
    lblcaone = tk.Label (master = fca, height = 1, font = ("Cambria", 20), fg = "red", bg = "green", width = 34, text = "- Cannolis -")
    lblcaone.pack ()
    lblcatwo = tk.Label (master = fca, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Cannolis are an Italian dessert with a special authentic cream wrapped in a\nlayer of sweet dough like a roll. Cannolis aren't really fast food, and only\nthe best cannolis are made in restaurants, mostly inside the restaurants that\nare authentic. Cannolis usually have chocolate shaving in them and can be\ndipped in chocolate sauce. They also can have powered sugar sprinkled on\ntop of them. The cream inside of them makes cannolis very hard to replicate.")
    lblcatwo.pack ()
    butca = tk.Button (master = fca, width = 72, bg = "gray", fg = "black", text = "Close Information")
    butca.pack ()
    def displayCa (event):
        fca.pack_forget ()
    butca.bind ("<Button-1>", displayCa)
butfour = tk.Button (master = ffour, bg = "gray", fg = "black", width = 31, font = ("Cambria", 11),text = "Lasagna")
butfour.pack(side = tk.RIGHT)
def displayFour (event):
    fla = tk.Frame (bg = "light gray")
    fla.pack ()
    lbllaone = tk.Label (master = fla, height = 1, font = ("Cambria", 20), fg = "red", bg = "green", width = 34, text = "- Lasagna -")
    lbllaone.pack ()
    lbllatwo = tk.Label (master = fla, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Lasagna is one of the Italian foods that is widespread throughout the entire\nworld. Lasagna consists of layers of meat sauce and have paster dividers in\nbetween the layers. On the top, is a layer of cheese, usually ricotta. Unlike\nsome other Italian Foods, you can buy frozen lasagna at some supermarkets\nand heat it up in the microwave, but it does not taste as good as the real\nthing. Lasagna also usually has herbs including basil as well as rosemary.")
    lbllatwo.pack ()
    butla = tk.Button (master = fla, width = 72, bg = "gray", fg = "black", text = "Close Information")
    butla.pack ()
    def displayLa (event):
        fla.pack_forget ()
    butla.bind ("<Button-1>", displayLa)

ffive = tk.Frame (bg = "light gray")
ffive.pack ()

butfive = tk.Button (master = ffive, bg = "gray", fg = "black", width = 31, font = ("Cambria", 11), text = "Risotto")
butfive.pack(side = tk.LEFT)
def displayFive (event):
    fis = tk.Frame (bg = "light gray")
    fis.pack ()
    lblisone = tk.Label (master = fis, height = 1, font = ("Cambria", 20), fg = "red", bg = "green", width = 34, text = "- Risotto -")
    lblisone.pack ()
    lblistwo = tk.Label (master = fis, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Risotto is a Italian dish that originated from Northern Italy that is rice\nboiled in broth until it's at a creamy consistency. The broth can be made from\n meat or vegetables, and many types include white wine or parmesan cheese in\nthe recipe. Risotto is the most common way how to make rice in Italy and\nwas originally white, but it now has expensive spices like saffron to give its\nyellow color. Risotto can now be bought in supermarkets in the US.")
    lblistwo.pack ()
    butis = tk.Button (master = fis, width = 72, bg = "gray", fg = "black", text = "Close Information")
    butis.pack ()
    def displayIs (event):
        fis.pack_forget ()
    butis.bind ("<Button-1>", displayIs)
butsix = tk.Button (master = ffive, bg = "gray", fg = "black", width = 31, font = ("Cambria", 11),text = "Acquacotta")
butsix.pack(side = tk.RIGHT)
def displaySix (event):
    fqu = tk.Frame (bg = "light gray")
    fqu.pack ()
    lblquone = tk.Label (master = fqu, height = 1, font = ("Cambria", 20), fg = "red", bg = "green", width = 34, text = "- Acquacotta -")
    lblquone.pack ()
    lblqutwo = tk.Label (master = fqu, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Acquacotta is an Italian peasant dish that's like a bread soup that's hot.\nIt was originally made to make stale bread edible, but it is now not used for\nthat purpose and its ingredients vary. Some variations include acquacotta con\npeperoni (aquacotta with peppers) and aquacotta con funghi (acquacotta with\nmushrooms). Other variations of this recipe inlcude sprinkling cheese on top\n(usually with parmigiano or pecorino cheese) and other vegetables.")
    lblqutwo.pack ()
    butqu = tk.Button (master = fqu, width = 72, bg = "gray", fg = "black", text = "Close Information")
    butqu.pack ()
    def displayAc (event):
        fqu.pack_forget ()
    butqu.bind ("<Button-1>", displayAc)

butone.bind ("<Button-1>", displayOne)
buttwo.bind ("<Button-1>", displayTwo)
butthree.bind ("<Button-1>", displayThree)
butfour.bind ("<Button-1>", displayFour)
butfive.bind ("<Button-1>", displayFive)
butsix.bind ("<Button-1>", displaySix)

window.mainloop ()