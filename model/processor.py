import time
import math
import threading	
import random
def generateInstruction(proc_number,probability):
	print("probablidad del hilo: "+str(proc_number)+"   es: " + str(probability))
	n = random.randint(0,50)
	if n < (probability*100):
		print("store")
	else:
		print("read")



def mainProcessor(proc_number,semaforo):
	x = 0
	lamb = int(proc_number)
	while x < 6:
		probability  = math.exp( -lamb )*((lamb**x)/(math.factorial(math.ceil(x))))
		time_to_slep = 10-20*probability
		#print("Thread "+proc_number+": whit the time "+str(time_to_slep))
		generateInstruction(proc_number,probability)
		if(proc_number == "1"):
			print(" probability                       "+str(probability)+" try "+str(x)+" buajjajaajaj")
		#time.sleep(0.1)
		time.sleep(time_to_slep)
		if x == 5:
			x = 0
		else:
			x += 0.1
			x = round(x,1)
	print(proc_number)
	#semaforo.acquire();
	print("Thread "+proc_number+" : start")
	time.sleep(2)
	print("Thread "+proc_number+" : finishing")
	#semaforo.release();
