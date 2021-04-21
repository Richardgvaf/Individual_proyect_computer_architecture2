import random
class cacheL1():
	def __init__(self):
		self._data1 = {'state':'I','mem_dir':'0','data': '0x0000'}
		self._data1 = {'state':'I','mem_dir':'0','data': '0x0000'}

	def get_data1(self):
		return self._data1
	
	def get_data2(self):
		return self._data2
	
	def set_data1(self,data1):
		self._data1 = data1;
	
	def set_data2(self,data2):
		self._data2 = data2

	def read_l1_value(self,instruction):
		if instruction['mem_dir'] == self._data1['mem_dir'] and self._data1['state'] != 'I':
			return self._data1['data']
		elif instruction['mem_dir'] == self._data2['mem_dir'] and self._data2['state'] != 'I':
			return self._data2['data']
		else:
			read_l2_value()
	def write_l1_value(self,instruction):
		if instruction['mem_dir'] == self._data1['mem_dir']:
			self._data1.setdefault("state","M")
			self._data1.setdefault('data',instruction['data'])
		elif instruction['mem_dir'] == self._data2['mem_dir']:
			self._data2.setdefault("state","M")
			self._data2.setdefault('data',instruction['data'])
		elif self._data1['state'] == 'I':
			self._data1.setdefault("state","M")
			self._data1.setdefault('data',instruction['data'])
		elif self._data2['state'] == 'I':
			self._data2.setdefault("state","M")
			self._data2.setdefault('data',instruction['data'])
		elif (self._data1['state'] == 'M') and (self._data2['state'] == 'M'):
			if random.randint(0,90) < 50:
				#####falta agregar el write_trought############
				self._data1.setdefault("state","M")
				self._data1.setdefault('data',instruction['data'])
			else:
				#####falta agregar el write_trought############
				self._data2.setdefault("state","M")
				self._data2.setdefault('data',instruction['data'])

	def write_in_cache_l1(self):

	def validate_data(self):

	def write_in_cache_l2(self):

