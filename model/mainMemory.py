import random
class mainMemory():
	def __init__(self,interface):
		self._data1 = {'mem_dir':'0','data': '0x0000'}
		self._data2 = {'mem_dir':'1','data': '0x0000'}
		self._data3 = {'mem_dir':'2','data': '0x0000'}
		self._data4 = {'mem_dir':'3','data': '0x0000'}
		self._data5 = {'mem_dir':'4','data': '0x0000'}
		self._data6 = {'mem_dir':'5','data': '0x0000'}
		self._data7 = {'mem_dir':'6','data': '0x0000'}
		self._data8 = {'mem_dir':'7','data': '0x0000'}
		self._interface = interface
		self.notify_interface()


	def modify_data(self,mem_dir,data):
		if mem_dir == 0:
			self._data1['data']=data
		if mem_dir == 1:
			self._data1['data']=data
		if mem_dir == 2:
			self._data2['data']=data
		if mem_dir == 3:
			self._data3['data']=data
		if mem_dir == 4:
			self._data4['data']=data
		if mem_dir == 5:
			self._data5['data']=data
		if mem_dir == 5:
			self._data5['data']=data
		if mem_dir == 6:
			self._data6['data']=data
		if mem_dir == 7:
			self._data7['data']=data
	

	
	def notify_interface(self):
		self._interface.put({'action':'memory',
			'data1':self._data1['data'],'mem_dir1':self._data1['mem_dir'],
			'data2':self._data2['data'],'mem_dir2':self._data2['mem_dir'],
			'data3':self._data3['data'],'mem_dir3':self._data3['mem_dir'],
			'data4':self._data4['data'],'mem_dir4':self._data4['mem_dir'],
			'data5':self._data5['data'],'mem_dir5':self._data1['mem_dir'],
			'data6':self._data6['data'],'mem_dir6':self._data2['mem_dir'],
			'data7':self._data7['data'],'mem_dir7':self._data7['mem_dir'],
			'data8':self._data8['data'],'mem_dir8':self._data8['mem_dir'],
			})