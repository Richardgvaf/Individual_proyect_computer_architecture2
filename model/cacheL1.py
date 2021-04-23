import random
import threading
import time
class cacheL1():
	def __init__(self,interface,semaphore,cache_l2):
		self._data1 = {'state':'I','mem_dir':'0','data': '0x0000'}
		self._data2 = {'state':'I','mem_dir':'0','data': '0x0000'}
		self._interface = interface
		self._semaphore = semaphore
		self._cache_l2  = cache_l2
		self.notify_interface()

	def read_l1_value(self,instruction):
		print("EL tipo es..... :")
		if (instruction['mem_dir'] == self._data1['mem_dir']) and self._data1['state'] == 'I':
			self.read_through(instruction['mem_dir'],'S',self._data1)

		elif instruction['mem_dir'] == self._data2['mem_dir'] and self._data2['state'] == 'I':
			self.read_through(instruction['mem_dir'],'S',self._data2) 
			
		elif (instruction['mem_dir'] != self._data1['mem_dir']) and (instruction['mem_dir'] != self._data2['mem_dir']):
			if random.randint(0,99) < 50:
				self.read_through(instruction['mem_dir'],'S',self._data1)
			else:
				self.read_through(instruction['mem_dir'],'S',self._data2)
		self.notify_interface()

	def read_through(self,mem_dir,state,selfData):
		time.sleep(0.3)
		self._semaphore.acquire()
		time.sleep(5)
		data = self._cache_l2.read_l2_value(mem_dir=mem_dir)
		self.replace_data(mem_dir,state,data,selfData)
		self._semaphore.release()
			
	def replace_data(self,mem_dir,state,data,selfData):
		selfData['mem_dir'] = mem_dir
		selfData['state']   = state
		selfData['data']    = data

	def replace_data1(self,mem_dir,state,data):
		self._data1['mem_dir'] = mem_dir
		self._data1['state']   = state
		self._data1['data']    = data

	def replace_data2(self,mem_dir,state,data):
		self._data2['mem_dir'] = mem_dir
		self._data2['state']   = state
		self._data2['data']    = data

	def write_trought(self,instruction):
		self._semaphore.acquire()
		time.sleep(5)
		self._cache_l2.write_l2_value(instruction=instruction)
		self._semaphore.release()
	
	def validate_writing(self,state,data):
		if data['state'] == 'M':
			data['state'] = state
			self.notify_interface()
			self.write_trought(data)
		data['state'] = state
		self.notify_interface()

	def read_notify(self,instruction):
		if (instruction['action'] == 'write') and (instruction['mem_dir'] == self._data1['mem_dir']):
			self.validate_writing('I',self._data1)

		if (instruction['action'] == 'write') and (instruction['mem_dir'] == self._data2['mem_dir']):
			self.validate_writing('I',self._data2)

		if (instruction['action'] == 'read') and (instruction['mem_dir'] == self._data1['mem_dir']):
			self.validate_writing('S',self._data1)

		if (instruction['action'] == 'read') and (instruction['mem_dir'] == self._data2['mem_dir']):
			self.validate_writing('S',self._data2)
		
	
	def notify_interface(self):
		self._interface.put({'action':'memory_l1','data1':self._data1['data'],'state1':self._data1['state'],'data2':self._data2['data'],'state2':self._data2['state'],'mem_dir2':self._data2['mem_dir'],'mem_dir1':self._data1['mem_dir']})
	
	def write_l1_value(self,instruction):
		#if data is in cache l1 overwrite
		if instruction['mem_dir'] == self._data1['mem_dir']:
			self.replace_data1(instruction['mem_dir'],"M",instruction['data'])

		elif instruction['mem_dir'] == self._data2['mem_dir']:
			self.replace_data2(instruction['mem_dir'],"M",instruction['data'])

		#if data is invalid override
		elif self._data1['state'] == 'I':
			self.replace_data1(instruction['mem_dir'],"M",instruction['data'])

		elif self._data2['state'] == 'I':
			self.replace_data2(instruction['mem_dir'],"M",instruction['data'])

		#if one is Shared and the other is modified replace the shared data
		elif (self._data1['state'] == 'S') and (self._data2['state'] == 'M'):
			self.replace_data1(instruction['mem_dir'],"M",instruction['data'])

		elif (self._data1['state'] == 'M') and (self._data2['state'] == 'S'):
			self.replace_data2(instruction['mem_dir'],"M",instruction['data'])

		#if both are modified write over L2 and then replace
		elif (self._data1['state'] == 'M') and (self._data2['state'] == 'M'):
			if random.randint(0,99) < 50:
				self.write_trought(self._data1)
				self.replace_data1(instruction['mem_dir'],"M",instruction['data'])
			else:
				self.write_trought(self._data2)
				self.replace_data2(instruction['mem_dir'],"M",instruction['data'])
		self.notify_interface()
		


