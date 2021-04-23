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

        #send messages to threads
        self._to_P0 = queue.Queue()
        self._to_P1 = queue.Queue()
        self._to_P2 = queue.Queue()
        self._to_P3 = queue.Queue()

        self._from_memory = queue.Queue()

        self._interface_queue = queue.Queue() 
        self._main_model = mainModel()
        self._main_model.main_model(from_P0=self._from_P0,from_P1=self._from_P1,from_P2=self._from_P2,from_P3=self._from_P3,memory=self._from_memory,to_P0=self._to_P0,to_P1=self._to_P1,to_P2=self._to_P2,to_P3=self._to_P3);
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
        self.display_instruction_writer()
        self.display_game_mode()
        self.constant_check()

    def display_game_mode(self):
        self._game_mode = 1
        self._game_mode_text = tk.StringVar()
        self._button_manual = tk.Button(text=self._game_mode_text, command=self.setMode)
        self._game_mode_text.set("Manual_mode")
        self._button_manual.place(x=530, y=20,  width = 200, height = 30)
    def setMode(self):
        if self._game_mode == 1:
            self._to_P0.put('manual')
            self._to_P1.put('manual')
            self._to_P2.put('manual')
            self._to_P3.put('manual')
            self._game_mode_text.set("Auto_mode")
            self._game_mode = 0
        else:
            self._to_P0.put('auto')
            self._to_P1.put('auto')
            self._to_P2.put('auto')
            self._to_P3.put('auto')
            self._game_mode_text.set("Manual_mode")
            self._game_mode = 1

    def display_instruction_writer(self):
        self._entryText = tk.StringVar()
        self._entry = tk.Entry(textvariable=self._entryText)
        self._entry.place(x=20, y=20,  width = 200, height = 30)
        self._button_send = tk.Button(text="Enviar instruction", command=self.send)
        self._button_send.place(x=230, y=20,  width = 200, height = 30)


    def send(self):
        text = self._entryText.get()
        text = text.split()
        if text[1] == "write":
            instruction = {'action':'write','mem_dir':text[2],'data':text[3] }
        if text[1] == "read":
            instruction = {'action':'read','mem_dir':text[2]}
        if text[1] == "calc":
            instruction = {'action':'calc'}
        if text[0]== "P0":
            self._to_P0.put(instruction)
        if text[0]== "P1":
            self._to_P1.put(instruction)
        if text[0]== "P2":
            self._to_P2.put(instruction)
        if text[0]== "P3":
            self._to_P3.put(instruction)
        print(text)
        self._entryText.set("")

    def instruction_processor(self,instruction):
        if instruction['action'] == "read":
            return "read " + instruction['mem_dir']
        if instruction['action'] == "write":
            return "write " + instruction['mem_dir']+"  "+instruction['data']
        if instruction['action'] == "calc":
            return "calc"


    def instruction_memoryl1(self,instruction,proc_number):
        self._caches[proc_number]['text']   = instruction['mem_dir1']+"   "+instruction['state1']+ '  ' + instruction['data1']
        self._caches[proc_number+4]['text'] = instruction['mem_dir2']+"   "+instruction['state2']+ '  ' + instruction['data2']


    def chek_processor(self):
        if self._from_P0.qsize() != 0:
            instruction = self._from_P0.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memoryl1(instruction,0)
            else:
                self._processors[0]['text'] = self.instruction_processor(instruction)

        if self._from_P1.qsize() != 0:
            instruction = self._from_P1.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memoryl1(instruction,1)
            else:
                self._processors[1]['text'] = self.instruction_processor(instruction)

        if self._from_P2.qsize() != 0:
            instruction = self._from_P2.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memoryl1(instruction,2)
            else:
                self._processors[2]['text'] = self.instruction_processor(instruction)
        if self._from_P3.qsize() != 0:
            instruction = self._from_P3.get()
            if instruction['action'] == 'memory_l1':
                self.instruction_memoryl1(instruction,3)
            else:
                self._processors[3]['text'] = self.instruction_processor(instruction)

    def set_memoryL2(self,instruction):
        self._l2_cache[0]['text']   = instruction['mem_dir1']+"   "+instruction['state1']+ '  ' + instruction['data1']
        self._l2_cache[1]['text']   = instruction['mem_dir2']+"   "+instruction['state2']+ '  ' + instruction['data2']
        self._l2_cache[2]['text']   = instruction['mem_dir3']+"   "+instruction['state3']+ '  ' + instruction['data3']
        self._l2_cache[3]['text']   = instruction['mem_dir4']+"   "+instruction['state4']+ '  ' + instruction['data4']

    def set_memory(self,instruction):
        print("values had change")
        self._memory[0]['text']  = instruction['mem_dir1']+"   " + instruction['data1']
        self._memory[1]['text']  = instruction['mem_dir2']+"   " + instruction['data2']
        self._memory[2]['text']  = instruction['mem_dir3']+"   " + instruction['data3']
        self._memory[3]['text']  = instruction['mem_dir4']+"   " + instruction['data4']
        self._memory[4]['text']  = instruction['mem_dir5']+"   " + instruction['data5']
        self._memory[5]['text']  = instruction['mem_dir6']+"   " + instruction['data6']
        self._memory[6]['text']  = instruction['mem_dir7']+"   " + instruction['data7']
        self._memory[7]['text']  = instruction['mem_dir8']+"   " + instruction['data8']

    def chek_memories(self):
        if self._from_memory.qsize() != 0:
            instruction = self._from_memory.get()
            if instruction['action'] == 'memory_l2':
                self.set_memoryL2(instruction)
            if instruction['action'] == 'memory':
                self.set_memory(instruction)


    def constant_check(self): 
        while True:
            self.chek_processor()
            self.chek_memories()
            self.update()
            time.sleep(0.1)   
    def display_background(self):
        imagen = PhotoImage(file = "images/fondo.png")
        background = tk.Label(image = imagen, text = "Imagen de fondo")
        background.place(x = 0, y = 0, width = 700, height = 500)
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
