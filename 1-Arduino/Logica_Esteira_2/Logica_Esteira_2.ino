//Carrega a biblioteca do sensor Ultrassonico
#include <Ultrasonic.h>

//Define os pinos para o trigger e echo
    //Sensor Ultrassônico 1 --> Onde o robô depositará a caixa
    #define pino_trigger 6 //AMARELO
    #define pino_echo 7 //VERDE
    //Sensor Ultrassônico 2 --> Onde o pedido será coletado pelo atendente
    #define pino_trigger_v1 8 //BRANCO
    #define pino_echo_v1 9 //AZUL

//Definicoes pinos Arduino ligados a entrada da Ponte H
int IN1 = 4;
int IN2 = 5;
int PWM = 3;
int vel = 0;
int Esteira_Ligada_Ida=0;

float Sensor1;
float Sensor2;

//Inicializa o sensor nos pinos definidos acima
Ultrasonic ultrasonic(pino_trigger, pino_echo);
Ultrasonic ultrasonic2(pino_trigger_v1, pino_echo_v1);

void setup(){
    Serial.begin(9600);
    //Define os pinos como saida
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(PWM, OUTPUT);
}
  
void loop(){
    
    // Leitura do Sensor 1
    long microsec = ultrasonic.timing();
    Sensor1 = ultrasonic.convert(microsec, Ultrasonic::CM);
    
    // Leitura do Sensor 2
    long microsec2 = ultrasonic2.timing();
    Sensor2 = ultrasonic2.convert(microsec2, Ultrasonic::CM);
  
    if (Sensor1 <= 10 && Esteira_Ligada_Ida == 0) {
        delay(4000);
        //Gira o Motor  no sentido horario
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        vel=0;
        Esteira_Ligada_Ida = 1;
        while(Sensor2>10){
            Sensor2 = ultrasonic2.convert(ultrasonic2.timing(), Ultrasonic::CM);
            if(vel<50){
              vel+=10;
              Serial.println(Sensor2);
            }
            analogWrite(PWM, vel);
            delay(150);
        }
    }
    
    else if(Sensor2<=10 && Esteira_Ligada_Ida == 1){
        //Freia o motor
        Esteira_Ligada_Ida = 0;
        //while(vel>0 && Sensor1>10){
            //vel-=50;
            analogWrite(PWM, 0);
            //delay(15);
            //Serial.println(Sensor2);
        //}
    }

    else{
        //Para o motor
        Esteira_Ligada_Ida = 0;
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, HIGH);
        Serial.println(Sensor2);
    }

}
