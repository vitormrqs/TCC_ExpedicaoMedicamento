//Controle do trabalho


//Definindo variáveis;
float ultima, contador,  x, cm, erro_atual, pos_atual, offset;
float i, j;
float erro_ant=0;
float pos_ant=25;
float motor_init = 100;

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
  
//Mantendo ultima ou substituindo;
  if (j<1000)
    x = ultima;
    else{
      ultima = contador/j;
      x = contador/j;
      }
  erro_atual = (x-offset);
  pos_atual = 0.8048*pos_ant+(+19.45*erro_atual-19.41*erro_ant)*1;
  
//Limitando o motor;
  //if (x < offset){
    if (pos_atual>10){
      pos_atual=10;
      }
    if (pos_atual<-10){
      pos_atual=-10;
      }
  myservo.write(motor_init-pos_atual);
//Limitando o motor;  
  if (cm>30){
    myservo.write(87);
    }
  if (cm<10){
    myservo.write(93);
    }
  
  //myservo.write(motor_init-pos_atual);
  erro_ant = erro_atual;
  pos_ant = pos_atual;
  Serial.print("Distancia: ");
  Serial.println(x);
}
//Equacao original de controle:
//pos=0.9048*pos_ant+19.45*erro_atual-19.41*erro_ant

