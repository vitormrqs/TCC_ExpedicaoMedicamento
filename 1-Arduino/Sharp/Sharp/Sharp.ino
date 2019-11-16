int sensorValue = 0;
int sensorPin = A0;
int i=0, j=0;
float contador, ultima, volts, cm;

void setup() {
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
}

void loop(){
    j=0;
    contador=0;
    for (i=0;i<200;i++){
        cm = 13864*pow(analogRead(sensorPin), -0.876);
        delay(1);
        if ((cm>130) and (cm<450)){
            j++;
            contador = cm + contador;
        }
    }
    ultima = contador/j;
    Serial.print("Valor Lido = ");
    Serial.print(ultima);
    Serial.println(" mm");

}
