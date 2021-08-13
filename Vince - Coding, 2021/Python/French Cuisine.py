import tkinter as tk
window = tk.Tk ()

f = tk.Frame (bg = "light gray")
f.pack ()

lblone = tk.Label (master = f, text = "- French Cuisine -", bg = "light green", fg = "white", width = 29, font = ("Cambria", 23))
lblone.pack ()
lbltwo = tk.Label (master = f, font = ("Cambria", 11), width = 61, bg = "light gray", text = "\nSearch in this database to find recognizable French foods and interesting\nfacts about them. This is not a restaurant website for ordering food.\n")
lbltwo.pack()

francais = tk.PhotoImage (file = "French Food1.png")
a = tk.Label (master = window, image = francais)
a.pack (side = tk.TOP)

ff = tk.Frame (bg = "light gray")
ff.pack ()

lblthree = tk.Label (master = ff, bg = "light gray", font = ("Cambria", 11), height = 1, width = 61, text = ("\n- Foods -\n"))
lblthree.pack ()

ftwo = tk.Frame (bg = "light gray")
ftwo.pack ()

butone = tk.Button (master = ftwo, bg = "gray", fg = "black", width = 34, text = "Croissants")
butone.pack(side = tk.LEFT)
def displayOne (event):
    fcr = tk.Frame (bg = "light gray")
    fcr.pack ()
    lblcrone = tk.Label (master = fcr, height = 1, font = ("Cambria", 15), fg = "white", bg = "light green", width = 45, text = "- Croissants -")
    lblcrone.pack ()
    lblcrtwo = tk.Label (master = fcr, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 61, text = "Croissants are French pastries that are made of French dough wrapped\nin the shape of a cresent. Croissants are usually coated in egg before\nput in the oven, making the outside crispy and crunchy. Croissants are\nusually plain, though sometimes they contain chocolate or a type of\njam. These pastries are usually served for breakast, and accompany coffee\nwell. Croissants can be found worldwide at bakeries and at patisseries.")
    lblcrtwo.pack ()
    butcr = tk.Button (master = fcr, width = 70, bg = "gray", fg = "black", text = "Close Information")
    butcr.pack ()
    def displayCr (event):
        fcr.pack_forget ()
    butcr.bind ("<Button-1>", displayCr)
buttwo = tk.Button (master = ftwo, bg = "gray", fg = "black", width = 34, text = "Macarons")
buttwo.pack(side = tk.RIGHT)
def displayTwo (event):
    fma = tk.Frame (bg = "light gray")
    fma.pack ()
    lblmaone = tk.Label (master = fma, height = 1, font = ("Cambria", 15), fg = "white", bg = "light green", width = 45, text = "- Macarons -")
    lblmaone.pack ()
    lblmatwo = tk.Label (master = fma, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 61, text = "Macarons are a French dessert made from two flavored French cookies\nwith a special type of filling compressed between the two cookies. They\nhave can come in many different flavors including, chocolate, mint,\ncoffee, caramel, and much more. Macarons are made by lightly cooking\ntwo cookies and by doing a very complicated process of aging egg whites.\nMacarons aren't really homemade and are usually bought at a store.")
    lblmatwo.pack ()
    butma = tk.Button (master = fma, width = 70, bg = "gray", fg = "black", text = "Close Information")
    butma.pack ()
    def displayMa (event):
        fma.pack_forget ()
    butma.bind ("<Button-1>", displayMa)
fthree = tk.Frame (bg = "light gray")
fthree.pack ()

butthree = tk.Button (master = fthree, bg = "gray", fg = "black", width = 34, text = "Escargot")
butthree.pack(side = tk.LEFT)
def displayThree (event):
    fes = tk.Frame (bg = "light gray")
    fes.pack ()
    lblesone = tk.Label (master = fes, height = 1, font = ("Cambria", 15), fg = "white", bg = "light green", width = 45, text = "- Escargot -")
    lblesone.pack ()
    lblestwo = tk.Label (master = fes, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 61, text = "Escargot is a dish that consists of edible snails that are cooked. They\nare usually covered in special herbs and can be served possibly as\nan hors d'oeuvre. Escargot is actually common thoughout the south of\nEurope, though French escargot is the best. Due to the demand for the\nescargot, there are massive snails farms in Europe and in the US. This\ndish is served at restaurants and can't really be found at supermarkets.")
    lblestwo.pack ()
    butes = tk.Button (master = fes, width = 70, bg = "gray", fg = "black", text = "Close Information")
    butes.pack ()
    def displayEs (event):
        fes.pack_forget ()
    butes.bind ("<Button-1>", displayEs)
butfour = tk.Button (master = fthree, bg = "gray", fg = "black", width = 34, text = "Filet Mignon")
butfour.pack(side = tk.RIGHT)
def displayFour (event):
    fil = tk.Frame (bg = "light gray")
    fil.pack ()
    lblilone = tk.Label (master = fil, height = 1, font = ("Cambria", 15), fg = "white", bg = "light green", width = 45, text = "- Filet Mignon -")
    lblilone.pack ()
    lbliltwo = tk.Label (master = fil, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 61, text = "Filet Mignon is French meat taken from a specific part of an animal near\nthe rib that is perhaps the best part of all. Filet Mignon can be\n covered in sauce or traditionally wrapped in another meat like bacon.\nFillet mignon can only be found in a small part of the cow, thus very\nexpensive. Filet mignon is usually either pork or beef and could be\ngrilled, broiled (sometimes in white wine), roasted, or pan-fried.")
    lbliltwo.pack ()
    butil = tk.Button (master = fil, width = 70, bg = "gray", fg = "black", text = "Close Information")
    butil.pack ()
    def displayIl (event):
        fil.pack_forget ()
    butil.bind ("<Button-1>", displayIl)

ffour = tk.Frame (bg = "light gray")
ffour.pack ()

butfive = tk.Button (master = ffour, bg = "gray", fg = "black", width = 34, text = "Quiche")
butfive.pack(side = tk.LEFT)
def displayFive (event):
    fqu = tk.Frame (bg = "light gray")
    fqu.pack ()
    lblquone = tk.Label (master = fqu, height = 1, font = ("Cambria", 15), fg = "white", bg = "light green", width = 45, text = "- Quiche -")
    lblquone.pack ()
    lblqutwo = tk.Label (master = fqu, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 61, text = "Quiche is basically an egg pie filled with a variety of ingredients.\nCrusts can vary in quiches, including crusts that are hard and crumbly\nand crusts that are soft and fluffy. Quiches can have many vegetables\nmeats inside them including sausage and bacon (for the meats), as well\nas spinach and onion (for the vegetables). Quiches also usually have\ncheese mixed with their egg, sometimes cheddar and pecorino.")
    lblqutwo.pack ()
    butqu = tk.Button (master = fqu, width = 70, bg = "gray", fg = "black", text = "Close Information")
    butqu.pack ()
    def displayQu (event):
        fqu.pack_forget ()
    butqu.bind ("<Button-1>", displayQu)
butsix = tk.Button (master = ffour, bg = "gray", fg = "black", width = 34, text = "Onion Soup Gratinee")
butsix.pack(side = tk.RIGHT)
def displaySix (event):
    fos = tk.Frame (bg = "light gray")
    fos.pack ()
    lblosone = tk.Label (master = fos, height = 1, font = ("Cambria", 15), fg = "white", bg = "light green", width = 45, text = "- Onion Soup Gratinee -")
    lblosone.pack ()
    lblostwo = tk.Label (master = fos, height = 7, font = ("Cambria", 10), fg = "black", bg = "light gray", width = 61, text = "Onion Soup Gratinee is a French soup that consists of meat broth and\nonions. In a fancy meal, the dish is served in the first course and can\nsometimes have a bread with cheese on top or croutons. The onions in\nthe soup are mainly carmalized when served, and the soup his served hot.\nThe soup usually has some white wine in it though it would be burnt\noff by the time that it is properly served in a bowl.")
    lblostwo.pack ()
    butos = tk.Button (master = fos, width = 70, bg = "gray", fg = "black", text = "Close Information")
    butos.pack ()
    def displayOs (event):
        fos.pack_forget ()
    butos.bind ("<Button-1>", displayOs)

butone.bind ("<Button-1>", displayOne)
buttwo.bind ("<Button-1>", displayTwo)
butthree.bind ("<Button-1>", displayThree)
butfour.bind ("<Button-1>", displayFour)
butfive.bind ("<Button-1>", displayFive)
butsix.bind ("<Button-1>", displaySix)

window.mainloop ()