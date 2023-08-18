const int pwm_out = 9;
const int s_stop = 10;
//**************************************************************************
//**************************************************************************
//**************************************************************************
void setup() {
  //Serial.begin(9600);
  pinMode(pwm_out,OUTPUT);
  pinMode(s_stop,OUTPUT);
  delay(100);
}
//**************************************************************************
//**************************************************************************
//**************************************************************************
void loop() {
  int sensorValue = analogRead(A0);
  //Serial.println(sensorValue);
  int D = map(sensorValue,0,1023,0,255);
  analogWrite(pwm_out,D);

  if (D<=28){
    digitalWrite(s_stop,HIGH);
    delay(100);
    digitalWrite(s_stop,LOW);
  }
  else{
    digitalWrite(s_stop,LOW);
  }
  
  delay(10);
}
