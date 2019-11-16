import threading
import DobotDllTypeTESTE as dType
#from config import available_ports, d, connectedPhysicalDobot
# from config import createDobotInterface
#from dobot import Dobot
# d=0
# available_ports=0
# connectedPhysicalDobot=0

initPose = [0,0,0,0,0,0,0,0]

def homePose():

	global initPose

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):

		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
		dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

		button  = dType.GetHHTTrigOutput(api)
		
		while not button:
			
			button  = dType.GetHHTTrigOutput(api)
			print("Define Init Position!")
			
			if button == 1:
				initPose = dType.GetPose(api)
				while initPose[0] == 0:
					initPose = dType.GetPose(api)
				print("Init Pose: ",initPose)

				dType.dSleep(2000) 
				lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,217.0, 0.0, 135.0 , 0.0, isQueued = 1)[0]
				#Start to Execute Command Queued
				dType.SetQueuedCmdStartExec(api)
				#Wait for Executing Last Command
				while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
					dType.dSleep(100)
				#Stop to Execute Command Queued
				dType.SetQueuedCmdStopExec(api)

		dType.DisconnectDobot(api)
	else:
		raise Exception("Dobot not connected!!")

def suctionCup(x):
	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):
		if x == 1:
			suction = True
		else:
			suction = False
		lastIndex = dType.SetEndEffectorSuctionCup(api, True,  suction, isQueued=0)
		dType.SetQueuedCmdStopExec(api)
		dType.DisconnectDobot(api)
	else:
		raise Exception
        
def hanoi(pick,place):
	pos = [0,0]
	
	if pick == 1:
		pos[0] = -200
	elif pick == 2:
		pos[0] = 0
	elif pick == 3:
		pos[0] = 200
		
	if place == 1:
		pos[1] = -200
	elif place == 2:
		pos[1] = 0
	elif place == 3:
		pos[1] = 200
		
	setPosition(pos[0],228,0,2)
	setPosition(pos[0],228,-50,2)
	suctionCup(1)
	setPosition(pos[0],228,0,2)
	
	setPosition(pos[1],228,0,2)
	setPosition(pos[1],228,-50,2)
	suctionCup(0)
	setPosition(pos[1],228,0,2)

def polinomial(x):

	global initPose

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):

		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
		dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
		
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, initPose[0], initPose[1], initPose[2], 0.0, isQueued = 1)[0]
		#scala = int(x/2) + 1
		#print("scala: ", scala)
		scala = x + 1
		for count in np.arange(0,scala,0.1):
			#x1 = ((count ** 2)*2)
			#y1 = count*2
			
			x1 = (count ** 2)*5
			y1 = count*5
	
			print("count", count)
			print("x: ", y1)
			print("y: ", x1)
			lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, (initPose[0] + x1 ), (initPose[1] - y1), initPose[2], 0.0, isQueued = 1)[0]
			#Start to Execute Command Queued
			dType.SetQueuedCmdStartExec(api)
			#Wait for Executing Last Command
			while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
				dType.dSleep(100)
			#Stop to Execute Command Queued
			dType.SetQueuedCmdStopExec(api)
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 217.0, 0.0, 135.0, 0.0, isQueued = 1)[0] 

		#Start to Execute Command Queued
		dType.SetQueuedCmdStartExec(api)
		#Wait for Executing Last Command
		while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			dType.dSleep(100)
		#Stop to Execute Command Queued
		dType.SetQueuedCmdStopExec(api)

		dType.DisconnectDobot(api)
	else:
		raise Exception


def setPosition(y1,x1,z1,moveType):

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):

		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
		dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

		lastIndex = dType.SetPTPCmd(api, moveType, x1, y1, z1, 0.0, isQueued = 1)[0]
		#lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]
		dType.dSleep(1)

		#Start to Execute Command Queued
		dType.SetQueuedCmdStartExec(api)
		#Wait for Executing Last Command
		while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			dType.dSleep(1)
		#Stop to Execute Command Queued
		dType.SetQueuedCmdStopExec(api)
		dType.DisconnectDobot(api)
	else:
		raise Exception

def arc(y, x, y1, x1, y2, x2):

	global initPose

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):

		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
		dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
		dType.SetARCParams(api,  200, 200, 200, 200,  isQueued = 1)
		
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, (initPose[0] + x), (initPose[1] - y), initPose[2], 0.0, isQueued = 1)[0]
		
		orin = [(initPose[0] + x),  (initPose[1] - y), initPose[2], 0]
		pos = [(initPose[0] + x1),  (initPose[1] - y1), initPose[2], 0]
		buff = [(initPose[0] + x2), (initPose[1] - y2), initPose[2], 0]
		lastIndex = dType.SetARCCmd(api,pos,buff, isQueued=1)[0]
		dType.dSleep(1500)
		print("orin: ",orin)
		print("pos: ",pos)
		print("buff: ",buff)
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 217.0, 0.0, 135.0, 0.0, isQueued = 1)[0] 

		#Start to Execute Command Queued
		dType.SetQueuedCmdStartExec(api)
		#Wait for Executing Last Command
		while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			dType.dSleep(100)
		#Stop to Execute Command Queued
		dType.SetQueuedCmdStopExec(api)

		dType.DisconnectDobot(api)
	else:
		raise Exception
