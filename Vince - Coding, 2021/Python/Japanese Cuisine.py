import tkinter as tk
window = tk.Tk ()

f = tk.Frame (bg = "light gray")
f.pack ()

lblone = tk.Label (master = f, text = "- Japanese Cuisine -", bg = "white", fg = "red", width = 25, font = ("Cambria", 24))
lblone.pack ()
lbltwo = tk.Label (master = f, font = ("Cambria", 11), height = 4, width = 56, text = "\nSearch in this window to find interesting Japanese foods (this is not a\nwebsite to order food). Please click buttons to access information.\n")
lbltwo.pack ()

boat = tk.PhotoImage (file = "Sushi Boat2.png")
a = tk.Label (master = window, image = boat)
a.pack (side = tk.TOP)

ftwo = tk.Frame (bg = "light gray")
ftwo.pack ()

lblthree = tk.Label (master = ftwo, text = "- Foods -", width = 56, font = ("Cambria", 11))
lblthree.pack ()

ff = tk.Frame (bg = "light gray")
ff.pack ()

butone = tk.Button (master = ff, bg = "gray", fg = "black", width = 27, font = ("Cambria", 11),text = "Sushi")
butone.pack(side = tk.LEFT)
def displayOne (event):
    fsh = tk.Frame (bg = "light gray")
    fsh.pack ()
    lblshone = tk.Label (master = fsh, height = 1, font = ("Cambria", 20), fg = "red", bg = "white", width = 30, text = "- Sushi -")
    lblshone.pack ()
    lblshtwo = tk.Label (master = fsh, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Sushi is one of the most important basic foods in Japan, and is basically\nrice wrapped in tight seaweed with ingredients inside. Some of these\ningredients include, shrimp, cucumber, spinach, mushroom, crab, cavaiar\nand much more. Sushi can be either raw or cooked and can have an exterior of\nseaweed or rice. Sushi is often dipped in soy sauce and is usually accompanied\nwith raw ginger and wasabi, though some people think wasabi is too spicy.")
    lblshtwo.pack ()
    butsh = tk.Button (master = fsh, width = 64, bg = "gray", fg = "black", text = "Close Information")
    butsh.pack ()
    def displaySh (event):
        fsh.pack_forget ()
    butsh.bind ("<Button-1>", displaySh)
buttwo = tk.Button (master = ff, bg = "gray", fg = "black", width = 27, font = ("Cambria", 11), text = "Tempura")
buttwo.pack(side = tk.RIGHT)
def displayTwo (event):
    ftm = tk.Frame (bg = "light gray")
    ftm.pack ()
    lbltmone = tk.Label (master = ftm, height = 1, font = ("Cambria", 20), fg = "red", bg = "white", width = 30, text = "- Tempura -")
    lbltmone.pack ()
    lbltmtwo = tk.Label (master = ftm, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Tempura is basically food fried in a Japanese way creating a coating around\nthe piece of food. Tempura can be anyhting from shrimp to brocolli, and\nworks with vegetables as well as meats. Tempura is customarily dipped\nin tempura sauce, though soy sauce works just fine. Tempura is usually made\nfrom shrimp, sweet potato, mushroom, and other foods, but it really works with\nanything. Tempura has to be fried in a certain way to make it nice and crisp.")
    lbltmtwo.pack ()
    buttm = tk.Button (master = ftm, width = 64, bg = "gray", fg = "black", text = "Close Information")
    buttm.pack ()
    def displayTm (event):
        ftm.pack_forget ()
    buttm.bind ("<Button-1>", displayTm)

fthree = tk.Frame (bg = "light gray")
fthree.pack ()

butthree = tk.Button (master = fthree, bg = "gray", fg = "black", width = 27, font = ("Cambria", 11), text = "Miso Soup")
butthree.pack (side = tk.LEFT)
def displayThree (event):
    fms = tk.Frame (bg = "light gray")
    fms.pack ()
    lblmsone = tk.Label (master = fms, height = 1, font = ("Cambria", 20), fg = "red", bg = "white", width = 30, text = "- Miso Soup -")
    lblmsone.pack ()
    lbltmtwo = tk.Label (master = fms, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Miso soup is a traditional soup in Japan that has usually has a yellwo hue.\nMiso soup can contain many things, though it usually contains scallions\nand tofu. Miso soup can be made at home with miso paste, but it would\nnot be as good. The soup is served hot, because if it was cold, it would\ntake away its flavor and the ingredients inside would be terribly bland. Miso\nsoup is very wet, so it is not recommended for you to dip your food in the soup.")
    lbltmtwo.pack ()
    butms = tk.Button (master = fms, width = 64, bg = "gray", fg = "black", text = "Close Information")
    butms.pack ()
    def displayMs (event):
        fms.pack_forget ()
    butms.bind ("<Button-1>", displayMs)
butfour = tk.Button (master = fthree, bg = "gray", fg = "black", width = 27, font = ("Cambria", 11), text = "Rice")
butfour.pack (side = tk.RIGHT)
def displayFour (event):
    fri = tk.Frame (bg = "light gray")
    fri.pack ()
    lblrione = tk.Label (master = fri, height = 1, font = ("Cambria", 20), fg = "red", bg = "white", width = 30, text = "- Rice -")
    lblrione.pack ()
    lblritwo = tk.Label (master = fri, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Rice is critically important in Japanese culture because a meal that doesn't\nhave rice would really be a Japanese meal. Rice is used in many dishes,\nmost notably sushi, and can be used in several other Japanese recipes.\nJapanese rice usually has a bit of vinegar in it to make it have a more\nsticky feeling (which is really helpful when making sushi) but it's sometimes\nleft alone usually when eating straight out of a bowl or a dough.")
    lblritwo.pack ()
    butri = tk.Button (master = fri, width = 64, bg = "gray", fg = "black", text = "Close Information")
    butri.pack ()
    def displayRi (event):
        fri.pack_forget ()
    butri.bind ("<Button-1>", displayRi)

ffour = tk.Frame (bg = "light gray")
ffour.pack ()

butfive = tk.Button (master = ffour, bg = "gray", fg = "black", width = 27, font = ("Cambria", 11), text = "Gyoza")
butfive.pack (side = tk.LEFT)
def displayFive (event):
    fgz = tk.Frame (bg = "light gray")
    fgz.pack ()
    lblgzone = tk.Label (master = fgz, height = 1, font = ("Cambria", 20), fg = "red", bg = "white", width = 30, text = "- Gyoza -")
    lblgzone.pack ()
    lblgztwo = tk.Label (master = fgz, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Gyoza is essentially pan fried Japanese dumplings that usually contain a meat\nlike pork or beef. Gyoza also usually contains scallions and is dipped in\n soy sauce. Gyoza is very different from dumplings due to it having a\nslightly more crunchy taste as well as having a more cooked inside.Gyoza\ncan be dipped in Tempura sauce too, though it's not recommended because it\ndoesn't taste as good. Wasabi does not accompany Gyoza well.")
    lblgztwo.pack ()
    butgz = tk.Button (master = fgz, width = 64, bg = "gray", fg = "black", text = "Close Information")
    butgz.pack ()
    def displayGz (event):
        fgz.pack_forget ()
    butgz.bind ("<Button-1>", displayGz)
butsix = tk.Button (master = ffour, bg = "gray", fg = "black", width = 27, font = ("Cambria", 11), text = "Ramen")
butsix.pack (side = tk.RIGHT)
def displaySix (event):
    fra = tk.Frame (bg = "light gray")
    fra.pack ()
    lblraone = tk.Label (master = fra, height = 1, font = ("Cambria", 20), fg = "red", bg = "white", width = 30, text = "- Ramen -")
    lblraone.pack ()
    lblratwo = tk.Label (master = fra, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 64, text = "Ramen isn't really an authentic Japanese food, but because it's very common in\nthe US, we'll talk about ramen. Ramen is basically a bowl full of noodles\nwith bits of meat inside (usually pork or beef) along with an egg in\nthe bowl. Ramen also usually have some greens floating around in the bowl\nand the whole thing is floating in a broth (usually chicken broth). Ramen\ncan be found all over the US, though it's not usually in restaurants.")
    lblratwo.pack ()
    butra = tk.Button (master = fra, width = 64, bg = "gray", fg = "black", text = "Close Information")
    butra.pack ()
    def displayRa (event):
        fra.pack_forget ()
    butra.bind ("<Button-1>", displayRa)

butone.bind ("<Button-1>", displayOne)
buttwo.bind ("<Button-1>", displayTwo)
butthree.bind ("<Button-1>", displayThree)
butfour.bind ("<Button-1>", displayFour)
butfive.bind ("<Button-1>", displayFive)
butsix.bind ("<Button-1>", displaySix)

window.mainloop ()