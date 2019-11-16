/*
O código apresenta o controle de uma plataforma utilizando um controlador de atraso de fase com as seguintes observações:

    *Tempo de resposta do sensor IR SHARP: 38+-10MS
    *Distâncias dos remédios originais:
        1º remédio: 135 mm
        2º remédio: 194 mm
        3º remédio: 267 mm
        4º remédio: 345 mm

        2º Medição:
        1º remédio: 138 mm
        2º remédio: 196 mm
        3º remédio: 272 mm
        4º remédio: 347 mm

UTF-8: ARDUINO
    48==0
    49==1
    50==2
    51==3

*/
#define RPWM 3
#define R_EN 4
#define R_IS 5
#define LPWM 6
#define L_EN 7
#define L_IS 8 
#define CW 1
#define CCW 0
#define debug 0
#include <RobojaxBTS7960.h>

RobojaxBTS7960 motor(R_EN, RPWM, R_IS, L_EN, LPWM, L_IS, debug);

int sensorValue = 0;
int sensorPin = A0;
int i=0, j=0, k=0;
int rem_1, rem_2, rem_3, rem_4;
float x, contador, ultima, volts, cm, erro_atual, pos_atual, offset, erro_ant, pos_ant;
int acao=0;
char str, data;

void setup() {
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
  motor.begin();
}

void loop() {    
    //InÍcio Serial
    char pos[5] = {'0','0','0','0','\0'};

    while (i<4){
        delay(15);
        if((Serial.available() > 0) && (i<4)) {
            data = Serial.read(); // Lê-se o caracter;
            pos[i]=data;
            if(pos[i]==49){ //GRAVAR FLAG PARA PEGAR REMEDIO_1;
                pos[i]='1';
                k+=1;
            }
            if(pos[i]==50){ //GRAVAR FLAG PARA PEGAR REMEDIO_2;
                pos[i]='2';
                k+=1;
            }
            if(pos[i]==51){ //GRAVAR FLAG PARA PEGAR REMEDIO_3;
                pos[i]='3';
                k+=1;
            }
            if(pos[i]==52){ //GRAVAR FLAG PARA PEGAR REMEDIO_4;
                pos[i]='4';
                k+=1;
            }
            i+=1;
        }
    }

    //Posicao dos remedios;
    rem_1=139;//136
    rem_2=195;//193.5
    rem_3=267;//267 271
    rem_4=345;//345
    
    //Bloco da posicao;
    if (pos[0]=='1'){
        offset=rem_1;
    }
    else if(pos[1]=='2'){
        offset=rem_2;
    }
    else if(pos[2]=='3'){
        offset=rem_3;
    }
    else if(pos[3]=='4'){
        offset=rem_4;
    }
    
    //Bloco da posição atual;
    for (i=0;i<50;i++){
        //cm = 13864*pow(analogRead(sensorPin), -0.876); //MDF
        cm = 7597*pow(analogRead(sensorPin), -0.781); //BRANCO
        delay(1);
        if ((cm>120) and (cm<360)){
            j++;
            contador = cm + contador;
        }
    }

    x = contador/j; //Onde estou;
    j=0;
    contador=0;

    i=0;

    /*Colocando Robo na posição inicial*/
    Serial.flush();
    Serial.print('0');   
    delay(1000); //VERIFICAR TEMPO



    /*Bloco de correção de posição*/
    while(k>0){
        //Bloco da posicao;
        if (pos[0]=='1'){
            offset=rem_1;
        }
        else if(pos[1]=='2'){
            offset=rem_2;
        }
        else if(pos[2]=='3'){
            offset=rem_3;
        }
        else if(pos[3]=='4'){
            offset=rem_4;
        }
        while((x>=offset*1.05) || (x<=offset*0.95)){
            //Bloco da posição atual;
            for (i=0;i<50;i++){
                //cm = 13864*pow(analogRead(sensorPin), -0.876);
                cm = 7597*pow(analogRead(sensorPin), -0.781); //BRANCO
                delay(1);
                if ((cm>120) and (cm<360)){
                    j++;
                    contador = cm + contador;
                }
            }

            x = contador/j; //Onde estou;
            j=0;
            contador=0;
        
            if(x>=offset*1.05){
                motor.stop();
                motor.rotate(40,CW);
            }
            else if (x<=offset*0.95){
                motor.stop();
                motor.rotate(40,CCW);
            }
        }

        motor.stop();
        
        //ROBO ATUA AQUI PEGANDO A CAIXA;
        if(offset==rem_1){
            Serial.flush();
            Serial.print('1');
            delay(4000);
        }
        else{
            Serial.flush();
            Serial.print('2');
            delay(4000);
        }
        
        //Levando plataforma para posição 4 e robô para esteira;
        offset=rem_4;
        Serial.print('3'); //ROBO VIRANDO PARA ESTEIRA;
        delay(6000);
        while((x>=offset*1.05) || (x<=offset*0.95)){
            for (i=0;i<50;i++){
                //cm = 13864*pow(analogRead(sensorPin), -0.876);
                cm = 7597*pow(analogRead(sensorPin), -0.781); //BRANCO
                delay(1);
                if ((cm>120) and (cm<360)){
                    j++;
                    contador = cm + contador;
                }
            }
            x = contador/j; //Onde estou;
            j=0;
            contador=0;
            if(x>=offset*1.05){
                motor.stop();
                motor.rotate(40,CW);
            }
            else if (x<=offset*0.95){
                motor.stop();
                motor.rotate(40,CCW);
            }
            else{
                motor.stop();
            }
        }
        Serial.print('4');  // ROBO DISPOE A CAIXA NA ESTEIRA E SOBE;
        delay(8500);       // TEMPO DO ROBOR POR A CAIXA NA ESTEIRA E SUBIR;
        if(pos[0]=='1'){
            pos[0]='0';
            k-=1;
        }
        else if(pos[1]=='2'){
            pos[1]='0';
            k-=1;
        }
        else if(pos[2]=='3'){
            pos[2]='0';
            k-=1;
        }
        else if(pos[3]=='4'){
            pos[3]='0';
            k-=1;
        }

    }

    /* BLOCO DE CONTROLE, AINDA NÃO IMPLEMENTADO;
    erro_atual = (x-offset); //Cálculo do erro
    pos_atual = (0.9999*pos_ant+(6.029*erro_atual-5.969*erro_ant)/7); //Equação de controle
    erro_ant = erro_atual; //Atualizacao de novos parametros
    pos_ant = pos_atual; //Atualizacao de novos parametros
    Serial.print("Valor Lido = ");
    Serial.print(x);
    Serial.println(" mm");
    */

}
