import traceback, serial, time

def serial_test():
    #Define a porta;pip
    ard = serial.Serial("COM6", 9600, timeout=5)
    print(ard.name)

    #Mensagem a ser printada;
    message = '49'
    print(message)

    #Método de escrita do Python para Arduino;
    ard.write(bytes('Hello World', 'UTF-8'))
    time.sleep(3)

    msg = ard.readline()
    print(msg)

if __name__ == "__main__":
    serial_test()