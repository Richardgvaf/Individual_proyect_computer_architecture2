from model.processor import *
import threading

class mainModel():
	def __init__(self):
		self._semaforo = threading.Semaphore(1);

	def main_model(self):
		processor1 = threading.Thread(target=mainProcessor, args=("1",self._semaforo,))
		processor1.start()
		processor2 = threading.Thread(target=mainProcessor, args=("2",self._semaforo,))
		processor2.start()
		processor3 = threading.Thread(target=mainProcessor, args=("3",self._semaforo,))
		processor3.start()
		processor4 = threading.Thread(target=mainProcessor, args=("4",self._semaforo,))
		processor4.start()
		return 'hello world Test'

