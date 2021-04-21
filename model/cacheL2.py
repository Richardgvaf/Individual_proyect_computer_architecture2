import random
class cacheL2():
	def __init__(self,interface):
		self._data1 = {'state':'DI','mem_dir':'0','data': '0x0000'}
		self._data2 = {'state':'DI','mem_dir':'0','data': '0x0000'}
		self._data3 = {'state':'DI','mem_dir':'0','data': '0x0000'}
		self._data4 = {'state':'DI','mem_dir':'0','data': '0x0000'}
		self._interface = interface
		self.notify_interface()


	def modify_data1(self,mem_dir,state,data):
		self._data1['mem_dir'] = mem_dir
		self._data1['state']   = state
		self._data1['data']    = data

	def modify_data2(self,mem_dir,state,data):
		if data2['state'] == 'DM':
			print("escribir en memoria")
		self._data2['mem_dir'] = mem_dir
		self._data2['state']   = state
		self._data2['data']    = data

	def modify_data3(self,mem_dir,state,data):
		self._data3['mem_dir'] = mem_dir
		self._data3['state']   = state
		self._data3['data']    = data

	def modify_data4(self,mem_dir,state,data):
		self._data4['mem_dir'] = mem_dir
		self._data4['state']   = state
		self._data4['data']    = data
	

	
	def notify_interface(self):
		self._interface.put({'action':'memory_l2',
			'data1':self._data1['data'],'state1':self._data1['state'],'mem_dir1':self._data1['mem_dir'],
			'data2':self._data2['data'],'state2':self._data2['state'],'mem_dir2':self._data2['mem_dir'],
			'data3':self._data3['data'],'state3':self._data3['state'],'mem_dir3':self._data3['mem_dir'],
			'data4':self._data4['data'],'state4':self._data4['state'],'mem_dir4':self._data4['mem_dir'],
			})
	
	def write_l2_value(self,instruction):
		#if data is in cache l1 overwrite
		if instruction['mem_dir'] == self._data1['mem_dir']:
			self.modify_data1(instruction['mem_dir'],"DM",instruction['data'])

		elif instruction['mem_dir'] == self._data2['mem_dir']:
			self.modify_data2(instruction['mem_dir'],"DM",instruction['data'])

		if instruction['mem_dir'] == self._data3['mem_dir']:
			self.modify_data3(instruction['mem_dir'],"DM",instruction['data'])

		elif instruction['mem_dir'] == self._data4['mem_dir']:
			self.modify_data4(instruction['mem_dir'],"DM",instruction['data'])

		#if data is invalid override
		elif self._data1['state'] == 'DI':
			self.modify_data1(instruction['mem_dir'],"DM",instruction['data'])

		elif self._data2['state'] == 'DI':
			self.modify_data2(instruction['mem_dir'],"DM",instruction['data'])

		elif self._data3['state'] == 'DI':
			self.modify_data3(instruction['mem_dir'],"DM",instruction['data'])

		elif self._data4['state'] == 'DI':
			self.modify_data4(instruction['mem_dir'],"DM",instruction['data'])
		else:
			random_replace = random.randint(0,99)
			if random_replace < 25:
				self.modify_data1(instruction['mem_dir'],"DM",instruction['data'])
			elif random_replace < 50:
				self.modify_data2(instruction['mem_dir'],"DM",instruction['data'])
			elif random_replace < 75:
				self.modify_data3(instruction['mem_dir'],"DM",instruction['data'])
			else:
				self.modify_data4(instruction['mem_dir'],"DM",instruction['data'])
		self.notify_interface()
		
