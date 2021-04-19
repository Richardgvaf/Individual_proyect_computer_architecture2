import tkinter as tk
from model.processor import *
import threading
from model.mainModel import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #Start the main model to int threads
        self._main_model = mainModel()
        self._main_model.main_model();
        
        self._processors = [0,0,0,0]
        self.master = master
        self.master.geometry("500x500")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def say_hi(self):
        print("hi there, everyone!")
    @property
    def display_processor(self,processor_number):
        x = 60
        y = 40
        width = 100
        height = 30
        self._processors[processor_number] = tk.Label(self)
        self._processors[processor_number]["text"] = "processor "+str(processor_number)
        self._processors[processor_number].place(x=x+processor_number*width, y=y, width=width, height=height)
        self._processors[processor_number].pack() 

