from model.processor import *
import threading,queue

class mainModel():
	def __init__(self):
		self._semaforo = threading.Semaphore(1);

		#define queues between processor to comunicate his messages
		self._p1_to_p2 = queue.Queue()
		self._p1_to_p3 = queue.Queue()
		self._p1_to_p4 = queue.Queue()

		self._p2_to_p1 = queue.Queue()
		self._p2_to_p3 = queue.Queue()
		self._p2_to_p4 = queue.Queue()

		self._p3_to_p1 = queue.Queue()
		self._p3_to_p2 = queue.Queue()
		self._p3_to_p4 = queue.Queue()

		self._p4_to_p1 = queue.Queue()
		self._p4_to_p2 = queue.Queue()
		self._p4_to_p3 = queue.Queue()

	def main_model(self,from_P0,from_P1,from_P2,from_P3):
		processor1 = threading.Thread(target=mainProcessor, args=(1,self._semaforo,self._p1_to_p2,self._p1_to_p3,self._p1_to_p4, self._p2_to_p1,self._p3_to_p1,self._p4_to_p1,from_P0,))
		processor1.start()
		processor2 = threading.Thread(target=mainProcessor, args=(2,self._semaforo,self._p2_to_p1,self._p2_to_p3,self._p2_to_p4, self._p1_to_p2,self._p3_to_p2,self._p4_to_p2,from_P1,))
		processor2.start()
		processor3 = threading.Thread(target=mainProcessor, args=(3,self._semaforo,self._p3_to_p1,self._p3_to_p2,self._p3_to_p4, self._p1_to_p3,self._p2_to_p3,self._p4_to_p3,from_P2,))
		processor3.start()
		processor4 = threading.Thread(target=mainProcessor, args=(4,self._semaforo,self._p4_to_p1,self._p4_to_p2,self._p4_to_p3, self._p1_to_p4,self._p2_to_p4,self._p3_to_p4,from_P3,))
		processor4.start()
		return 'hello world Test'

