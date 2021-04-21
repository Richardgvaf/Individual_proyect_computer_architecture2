import tkinter as tk
from tkinter import PhotoImage
from model.processor import *
import queue
from model.mainModel import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #Start the main model to int threads
        self._from_P0 = queue.Queue()
        self._from_P1 = queue.Queue()
        self._from_P2 = queue.Queue()
        self._from_P3 = queue.Queue()

        self._interface_queue = queue.Queue() 
        self._main_model = mainModel()
        self._main_model.main_model(from_P0=self._from_P0,from_P1=self._from_P1,from_P2=self._from_P2,from_P3=self._from_P3);
        self._processors = [0,0,0,0]
        self._caches = [0,0,0,0,0,0,0,0]
        self._l2_cache = [0,0,0,0]
        self._memory = [0,0,0,0,0,0,0,0]

        self.master = master
        self.master.geometry("600x500")
        self.display_background()
        self.display_caches()
        self.display_processor()
        self.display_l2_memory()
        self.display_memory()
        self.constant_check()

    def instruction_processor(self,instruction):
        if instruction['action'] == "read":
            return "read " + instruction['mem_dir']
        if instruction['action'] == "write":
            return "write " + instruction['mem_dir']+"  "+instruction['data']


    def instruction_memory(self,instruction,proc_number):
        self._caches[proc_number]['text']   = instruction['mem_dir1']+"   "+instruction['state1']+ '  ' + instruction['data1']
        self._caches[proc_number+4]['text'] = instruction['mem_dir2']+"   "+instruction['state2']+ '  ' + instruction['data2']


    def chek_processor(self):
        if self._from_P0.qsize() != 0:
            instruction = self._from_P0.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memory(instruction,0)
            else:
                self._processors[0]['text'] = self.instruction_processor(instruction)

        if self._from_P1.qsize() != 0:
            instruction = self._from_P1.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memory(instruction,1)
            else:
                self._processors[1]['text'] = self.instruction_processor(instruction)

        if self._from_P2.qsize() != 0:
            instruction = self._from_P2.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memory(instruction,2)
            else:
                self._processors[2]['text'] = self.instruction_processor(instruction)
        if self._from_P3.qsize() != 0:
            instruction = self._from_P3.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memory(instruction,3)
            else:
                self._processors[3]['text'] = self.instruction_processor(instruction) 
    def constant_check(self): 
        while True:
            self.chek_processor()
            self.update()
            time.sleep(0.1)   
    def display_background(self):
        imagen = PhotoImage(file = "images/fondo.png")
        background = tk.Label(image = imagen, text = "Imagen de fondo")
        background.place(x = 0, y = 0, width = 600, height = 500)
    def display_caches(self):
        x = 100
        y = 150
        width = 120
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
        width = 120
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
        x = 100
        y = 250
        width = 120
        height = 30
        self._l2_cache[0] = tk.Label()
        self._l2_cache[0]["text"] = "0    +   0 "
        self._l2_cache[0].place(x=x, y=y, width=width, height=height)

        self._l2_cache[1] = tk.Label()
        self._l2_cache[1]["text"] = "0    +   0 "
        self._l2_cache[1].place(x=x, y=(y+height), width=width, height=height)

        self._l2_cache[2] = tk.Label()
        self._l2_cache[2]["text"] = "0    +   0 "
        self._l2_cache[2].place(x=x, y=(y+height*2), width=width, height=height)

        self._l2_cache[3] = tk.Label()
        self._l2_cache[3]["text"] = "0    +   0 "
        self._l2_cache[3].place(x=x, y=(y+height*3), width=width, height=height)

    def display_memory(self):
        x = 300
        y = 250
        width = 120
        height = 30
        self._memory[0] = tk.Label()
        self._memory[0]["text"] = "0    +   0 "
        self._memory[0].place(x=x, y=y, width=width, height=height)

        self._memory[1] = tk.Label()
        self._memory[1]["text"] = "0    +   0 "
        self._memory[1].place(x=x, y=(y+height), width=width, height=height)

        self._memory[2] = tk.Label()
        self._memory[2]["text"] = "0    +   0 "
        self._memory[2].place(x=x, y=(y+height*2), width=width, height=height)

        self._memory[3] = tk.Label()
        self._memory[3]["text"] = "0    +   0 "
        self._memory[3].place(x=x, y=(y+height*3), width=width, height=height)

        self._memory[4] = tk.Label()
        self._memory[4]["text"] = "0    +   0 "
        self._memory[4].place(x=x, y=(y+height*4), width=width, height=height)

        self._memory[5] = tk.Label()
        self._memory[5]["text"] = "0    +   0 "
        self._memory[5].place(x=x, y=(y+height*4), width=width, height=height)

        self._memory[6] = tk.Label()
        self._memory[6]["text"] = "0    +   0 "
        self._memory[6].place(x=x, y=(y+height*5), width=width, height=height)

        self._memory[7] = tk.Label()
        self._memory[7]["text"] = "0    +   0 "
        self._memory[7].place(x=x, y=(y+height*6), width=width, height=height)
