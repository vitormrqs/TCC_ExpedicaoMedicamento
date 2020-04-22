# Expedição de Medicamentos
O conteúdo aqui presente aborda os códigos que foram utilizados durante o trabalho de graduação no Instituto Mauá de Tecnologia durante o ano de 2019. Os arquivos que _não estão comentados_ não foram criados por nós e sim pelo sistema ou programa utilizado.

## Programas necessários
Foram utilizados para construir o código:
- SQLite3;
- Python 3;
- Eric6;
- PyQt5;
- Arduino.

## Arquivos principais
### 1. Arduino 
Dentro da pasta `1-Arduino` existe:
- **BallBeam/BallBeam**: Foi um projeto anterior realizado no quinto ano da faculdade sobre o controle de uma bola utilizando PID. Foi utilizado como apoio no código para construção do projeto.
- **Controlador**: Tentativa de utilização de um controlador no sistema.
- **Logica_Esteira**: Primeira implementação da lógica da esteira presente no projeto.
- **Logica_Esteira_2**: Implementação final da lógica da esteira presente no projeto.
- **PegarCurvaSensor/AnalogInOutSerial**: Programa utilizado para entender a comunicação serial do robô com nosso programa em python. 
- **Rev12**: Arquivos utilizados no programa para o robô manipular os medicamentos.

### 2. PosicionamentoRobo/DobotPython
Dentro da pasta `2.PosicionamentoRobo/DobotPython`, existe:
#### Registros para utilizar o Dobot:
- DobotControl.py
- DobotDll.dll
- DobotDll.exp
- DobotDll.lib
- DobotDllType.py
- DobotDllTypeTESTE.py
- functions.pyc
- hanoi.py
- msvcp120.dll
- msvcr120.dll
- notepad++_macro.txt
- parametros salvos.txt

#### Registros para utilizar o PyQt5:
- Qt5Core.dll
- Qt5Network.dll
- Qt5SerialPort.dll

#### Programação utilizada:
- **Separacao_Caixa.py**: Programa utilizado para separação da caixa.
- Teste.py
- automatizado.py
- functions.py

### 3. ui
Todo conteúdo da pasta `ui` indica a geometria utilizada e criada por meio do `PyQt5`.

### Demais arquivos da raíz
Os demais arquivos da pasta raíz são:

- **0-Configuracao_GPIO.py**: Programa para criação de configuração da GPIO;
- **Database1.py**: Programa para geração do banco de dados;
- DobotDll.dll: Arquivo de registro do robô;
- DobotDll.exp: Arquivo de registro do robô;
- DobotDll.lib: Arquivo de lib do robô;
- DobotDllTypeTESTE.py: Arquivo de teste do robô;
- **Estoque.csv**: Planilha que o programa exporta como resultado do estoque utilizado;
- **H3V.e4p**: Programa utilizado no projeto;
- **estoque.db**: Arquivo do banco de dados utilizado;
- functions.py
- net0.py
- **program.py**: Programa utilizado no projeto;
- teste.py

# Autores
    Grupo: CAN01 - Expedição automatizada de medicamentos em hospitais.
- Higor Sanchez Dare
- Vinicius Diniz Coe
- Victor Costa do Nascimento
- Vitor Marques

# Licença
O seguinte projeto possui a licença GNU General Public License v3.0.
