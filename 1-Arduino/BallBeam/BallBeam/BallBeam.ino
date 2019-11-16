#include <Ultrasonic.h>
#include <Servo.h>

//Define os pinos para o trigger e echo;
#define pino_trigger 12 //marrom
#define pino_echo 13 //roxo

//Definindo variáveis;
float ultima, contador,  x, cm, erro_atual, pos_atual, offset;
float i, j;
float erro_ant=0;
float pos_ant=25;
float motor_init = 100;

Ultrasonic ultrasonic(pino_trigger, pino_echo);
Servo myservo;

void setup(){
  Serial.begin(9600);
  myservo.attach(9);
}
 
void loop(){
  double microsec = ultrasonic.timing();
//Zerando;
  contador=0;
  j=0;
  offset=25;
  
//Média para e obter um valor 'preciso' do sensor ultrassonico;
  for (i=0;i<1000;i++){
    cm = ultrasonic.convert(microsec, Ultrasonic::CM);
    if ((cm<30) and (cm>10)){
    j++;
    contador = cm + contador;
    }
  }
//Mantendo ultima medida ou substituindo;
  if (j<1000)
    x = ultima;
    else{
      ultima = contador/j;
      x = contador/j;
      }
      
  //Novo erro;   
  erro_atual = (x-offset);
  
  //Equacao de controle com ajuste do ganho /7;
  pos_atual = (0.8048*pos_ant+(+19.45*erro_atual-19.41*erro_ant)/7);
  
  //Escrita no motor;          
  myservo.write(motor_init-pos_atual);
  
  //Serial.println(pos_atual);
//Limitando o motor;  
  if (cm>28){
    myservo.write(80);
    }

  erro_ant = erro_atual;
  pos_ant = pos_atual;
  Serial.print("Distancia: ");
  Serial.println(x);
}
