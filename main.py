from view.mainView import *


root = tk.Tk()
app = Application(master=root)
imagen = PhotoImage(file = "images/fondo.png")
#background = tk.Label(root,image = imagen, text = "Imagen de fondo")
#background.pack()
#background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
app.mainloop()