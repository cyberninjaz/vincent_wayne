import tkinter as tk
window = tk.Tk()

c = tk.Canvas (bg = "light gray")

garden = tk.PhotoImage (file = "Garden1.png")
image = c.create_image (50, 50, image = garden )

c.pack()

window.mainloop()