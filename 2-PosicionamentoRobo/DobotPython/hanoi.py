from functions import *

setPosition(0,208,50,2)
while True:
	try:
		hanoi(1,2)
		hanoi(1,3)
		hanoi(2,3)
		hanoi(1,2)
		hanoi(3,1)
		hanoi(3,2)
		hanoi(1,2)
        
		hanoi(2,1)
		hanoi(2,3)
		hanoi(1,3)
		hanoi(2,1)
		hanoi(3,2)
		hanoi(3,1)
		hanoi(2,1)
	except KeyboardInterrupt:
		exit("Disconneted!")

