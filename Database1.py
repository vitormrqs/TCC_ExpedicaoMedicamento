import sqlite3

def TabEstoque():
    connection = sqlite3.connect("estoque.db")
    connection.execute("CREATE TABLE IF NOT EXISTS ESTOQUE(PEDIDO INT PRIMARY KEY, DATA TEXT, MEDICO TEXT, PACIENTE TEXT, REM1 INT, REM2 INT, REM3 INT, REM4 INT, FLAG TEXT)")
    connection.execute("INSERT INTO ESTOQUE VALUES(?,?,?,?,?,?,?,?,?)", (0, '0', '0',  '0', 100, 100, 100, 100, '0'))
    connection.commit()
    registros=connection.execute("SELECT * FROM ESTOQUE")
    for data in registros:
        print ("Pedido: ",  data[0])
        print ("Data: ",  data[1])
        print ("Medico: ",  data[2])
        print ("Paciente: ",  data[3])
        print ("Medicamento N1: ",  data[4])
        print ("Medicamento N2: ",  data[5])
        print ("Medicamento N3: ",  data[6])
        print ("Medicamento N4: ",  data[7])
        print ("Flag: ",  data[7])
    connection.close()
TabEstoque()
