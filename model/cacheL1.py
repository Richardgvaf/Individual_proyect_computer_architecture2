import random
class cacheL1():
	def __init__(self,interface):
		self._data1 = {'state':'I','mem_dir':'0','data': '0x0000'}
		self._data2 = {'state':'I','mem_dir':'0','data': '0x0000'}
		self._interface = interface

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
	def replace_data1(self,mem_dir,state,data):
		self._data1['mem_dir'] = mem_dir
		self._data1['state']   = state
		self._data1['data']    = data

	def replace_data2(self,mem_dir,state,data):
		self._data2['mem_dir'] = mem_dir
		self._data2['state']   = state
		self._data2['data']    = data
	def alert(self,instruction):
		if (instruction['action'] == write) and (instruction['mem_dir'] == self._data1['mem_dir']):
			#nota falta hacer write trought
			self.data1['state'] = "I" 
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
			if random.randint(0,90) < 50:
				#####falta agregar el write_trought############
				self.replace_data1(instruction['mem_dir'],"M",instruction['data'])
			else:
				#####falta agregar el write_trought############
				self.replace_data2(instruction['mem_dir'],"M",instruction['data'])
		self._interface.put({'action':'memory_l1','data1':self._data1['data'],'state1':self._data1['state'],'data2':self._data2['data'],'state2':self._data2['state'],'mem_dir2':self._data2['mem_dir'],'mem_dir1':self._data1['mem_dir']})

	def write_in_cache_l1(self):
		print("hello")

	def validate_data(self):
		print("hello")

	def write_in_cache_l2(self):
		print("hello")

