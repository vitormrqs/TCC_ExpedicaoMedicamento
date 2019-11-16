import threading
import DobotDllTypeTESTE as dType
#from config import available_ports, d, connectedPhysicalDobot
# from config import createDobotInterface
#from dobot import Dobot
# d=0
# available_ports=0
# connectedPhysicalDobot=0

initPose = [0,0,0,0,0,0,0,0]


def suctionCup(x):
	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "COM6", 115200)[0]
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


def setPosition(y1,x1,z1,moveType):

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "COM6", 115200)[0]
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
