import tkinter as tk
from tkinter import PhotoImage
from model.processor import *
import queue
from model.mainModel import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #Start the main model to int threads
        self._interface_queue = queue.Queue() 
        self._main_model = mainModel()
        self._main_model.main_model(interface_queue=self._interface_queue);
        self._processors = [0,0,0,0]
        self._caches = [0,0,0,0,0,0,0,0]
        self._l2_cache = [0,0,0,0]
        self.master = master
        self.master.geometry("600x500")
        self.display_background()
        self.display_caches()
        self.display_processor()

        

    def constant_check():
        while True:
            print("leer cola")
            time.sleep(30)
    def display_background(self):
        imagen = PhotoImage(file = "images/fondo.png")
        background = tk.Label(image = imagen, text = "Imagen de fondo")
        background.place(x = 0, y = 0, width = 600, height = 500)
    def display_caches(self):
        x = 100
        y = 150
        width = 100
        height = 30
        self._caches[0] = tk.Label()
        self._caches[0]["text"] = "data : "+"value"
        self._caches[0].place(x=x, y=y, width=width, height=height)

        self._caches[1] = tk.Label()
        self._caches[1]["text"] = "data1 : "+"value"
        self._caches[1].place(x=(x+width), y=y, width=width, height=height)
        
        self._caches[2] = tk.Label()
        self._caches[2]["text"] = "data2 : "+"value"
        self._caches[2].place(x=(x+width*2), y=y, width=width, height=height)
        
        self._caches[3] = tk.Label()
        self._caches[3]["text"] = "data3 : "+"value"
        self._caches[3].place(x=(x+width*3), y=y, width=width, height=height)

        self._caches[4] = tk.Label()
        self._caches[4]["text"] = "data : "+"value"
        self._caches[4].place(x=x, y=(y+height), width=width, height=height)

        self._caches[5] = tk.Label()
        self._caches[5]["text"] = "data1 : "+"value"
        self._caches[5].place(x=(x+width), y=(y+height), width=width, height=height)
        
        self._caches[6] = tk.Label()
        self._caches[6]["text"] = "data2 : "+"value"
        self._caches[6].place(x=(x+width*2), y=(y+height), width=width, height=height)
        
        self._caches[7] = tk.Label()
        self._caches[7]["text"] = "data3 : "+"value"
        self._caches[7].place(x=(x+width*3), y=(y+height), width=width, height=height)
        
    def display_processor(self):
        x = 100
        y = 100
        width = 100
        height = 30
        self._processors[0] = tk.Label()
        self._processors[0]["text"] = "P0 "
        self._processors[0].place(x=x, y=y, width=width, height=height)

        self._processors[1] = tk.Label()
        self._processors[1]["text"] = "P1 "
        self._processors[1].place(x=x+width, y=y, width=width, height=height)

        self._processors[2] = tk.Label()
        self._processors[2]["text"] = "P2 "
        self._processors[2].place(x=x+width*2, y=y, width=width, height=height)

        self._processors[3] = tk.Label()
        self._processors[3]["text"] = "P3 "
        self._processors[3].place(x=x+width*3, y=y, width=width, height=height)
    def display_l2_memory(self):
        self._l2_cache[0] = tk.Label()
         

