import time
import math
import threading	
import random
from model.cacheL1 import *

def generateInstruction(proc_number,probability):
	print("probablidad del hilo: "+str(proc_number)+"   es: " + str(probability))
	#Calculate the probability of each one and scale the result for a factor of 2.27 to complete one hundred percent
	probability1 = calcProbability(2,4)*100*2.27
	probability2 = calcProbability(3,4)*100*2.27
	probability3 = calcProbability(4,4)*100*2.27
	
	calc_prob = probability1
	store_prob  = calc_prob+probability2
	read_prob  = store_prob + probability3
	random_value = random.randint(0,99)

	instruction = {}
	instruction.setdefault("proc_number",str(proc_number))
	if random_value < calc_prob:
		instruction.setdefault("action","calc")
	elif random_value < store_prob:
		instruction.setdefault("action","write")
		random_dir = random.randint(0,7)
		instruction.setdefault("mem_dir",str(random_dir))
		random_data = hex(random.randint(0,1048575))
		instruction.setdefault("data",str(random_data))
	else:
		instruction.setdefault("action","read")
		random_dir = random.randint(0,7)
		instruction.setdefault("mem_dir",str(random_dir))
	return instruction

def notify(instruction,send_way1,send_way2,send_way3):
	if instruction == "write" or instruction == "read":
		send_way1.put(instruction)
		send_way2.put(instruction)
		send_way3.put(instruction)

def readNotify(recive_way1,recive_way2,recive_way3):
	print("read")

def writeL1(instruction, cache_l1):
	cache_l1.write_l1_value();

def writeThrough(semaphore):
	semaphore.acquire();
	print("Escribiendo en memoria L2");
	time.sleep(5)
	semaphore.release();

def writeThrough_l2():
	print("write_through_l2")
	time.sleep(10)

def calcProbability(lamb,k):
	probability  = math.exp( -lamb )*((lamb**k)/(math.factorial(math.ceil(k))))
	return probability

def manage_mem_instruction(instruction,cache_l1):
	if instruction['action'] == 'write':
		cache_l1.write_l1_value(instruction = instruction)

def mainProcessor(proc_number,semaforo,send_way1,send_way2,send_way3, recive_way1,recive_way2,recive_way3,interface):
	x = 0
	lamb = int(proc_number)
	cache_l1 = cacheL1(interface)
	while x < 6:
		#calculate the probability in each cycle that a delay appears 
		probability  = calcProbability(lamb,x)
		time_to_slep = 10-20*probability
		
		instruction = generateInstruction(proc_number,probability)
		interface.put(instruction)
		manage_mem_instruction(instruction,cache_l1)
		print("Queue size:  "+str(interface.qsize()))
		print(instruction)
		time.sleep(time_to_slep)
		notify(instruction,send_way1,send_way2,send_way3)
		
		#reset the cycle
		if x == 5:
			x = 0
		x += 0.1
		x = round(x,1)
	print(proc_number)
	#semaforo
	print("Thread "+proc_number+" : start")
	time.sleep(2)
	print("Thread "+proc_number+" : finishing")
	#semaforo.release();
