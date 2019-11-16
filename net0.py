import serial, time
from functions import *

def serial_tes():
    acao='a'
    arduino = serial.Serial('COM7', 9600, timeout=.1)
    time.sleep(2)
    arduino.write(bytes('1030', 'UTF-8')) #MANDOU COMANDO

    #acao = arduino.readline()
    #acao = str(acao)[2:3]
    #print(data)

    #if(acao=='0'):
    #    suctionCup(0)
    #    setPosition(35,90,-10,4) #Posição prepara para pegar caixa elevada
    while(acao != 'x'):
        time.sleep(1)
        acao = arduino.readline()
        time.sleep(1)
        aux = str(acao)[2:3]
        if(aux=='0'):
            suctionCup(0)
            setPosition(35,90,-10,4) #Posição prepara para pegar caixa elevada
        elif(aux=='1'): #Pegar caixa 1 - Pega em ângulo
            setPosition(35,94,26,4) #Posição pega caixa
            suctionCup(1)
            time.sleep(1) #RETIRAR
            suctionCup(0) #RETIRAR
            setPosition(35,94,-7,4) #Posição levanta caixa pega
            time.sleep(2)
            arduino.write(bytes('1', 'UTF-8'))
        elif(aux=='2'): #Pegar caixa 2,3 ou 4 - Pega em 90°
            setPosition(35,90,26,4)
            suctionCup(1)
            time.sleep(1) #RETIRAR
            suctionCup(0) #RETIRAR
            setPosition(35,90,-7,4) #Posição levanta caixa pega
            #arduino.write(bytes(str(1), 'UTF-8'))
        elif(aux=='3'): #Levar robô para posição de dispensa (verificar se pode ser implementada junto ao passo anterior)
            setPosition(0,-65,-7,4)
            arduino.write(bytes('2', 'UTF-8'))
        elif(aux=='4'): #Levar robô para posição de dispensa (verificar se pode ser implementada junto ao passo anterior)
            setPosition(32,-65,35,4) #Posição descarrega caixa
            suctionCup(0) #Solta caixa
            setPosition(33,-65,20,4) #Posição levanta robô para sair
            setPosition(35,90,-10,4) #Posição prepara para pegar caixa elevada
            arduino.write(bytes(str(3), 'UTF-8'))
            acao='x'


if __name__ == "__main__":
    serial_tes()
