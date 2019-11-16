from functions import *
import time

pega = 0
descarga = 0
caixa = 2
suctionCup(0)

#Posição 0
setPosition(0,0,0,4)

#Posição prepara para pegar caixa elevada
setPosition(35,90,-10,4)

#Verifica se é a caixa 1 que vai ser pega
if(caixa==1) :
	#Posição pega caixa
	setPosition(35,94,26,4)
	suctionCup(1)
	#Posição levanta caixa pega
	setPosition(35,94,-7,4)
else:
	#Posição pega caixa
	setPosition(35,90,26,4)
	suctionCup(1)
	#Posição levanta caixa pega
	setPosition(35,90,-7,4)

#Posição suspensa descarrega caixa
setPosition(0,-65,-7,4)

#Posição descarrega caixa
setPosition(32,-65,35,4)
suctionCup(0)

#Posição levanta robô para sair
setPosition(33,-65,20,4)

#Posição 0
setPosition(0,0,0,4)
