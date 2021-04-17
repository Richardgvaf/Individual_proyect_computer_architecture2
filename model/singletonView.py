import tkinter as tk
from view.mainView import *
class SingletonMeta(type):

    _instances = {}

    def __call__(self, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if self not in self._instances:


            self._root = tk.Tk()
            self._app = Application(master=self._root)
            

            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        self._app.mainloop()

        






