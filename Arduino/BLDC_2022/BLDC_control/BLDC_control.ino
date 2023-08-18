const int vel = 11;
const int dir = 12;
const int sA =  2;
const int sB =  3;
const int sC =  4;
const int Q0 = 5;
const int Q1 = 6;
const int Q2 = 7;
const int Q3 = 8;
const int Q4 = 9;
const int Q5 = 10;
int Q_out[7][6] = {{0,0,0,1,1,0},{1,0,0,1,0,0},{1,0,0,0,0,1},{0,0,1,0,0,1},{0,1,1,0,0,0},{0,1,0,0,1,0},{0,0,0,0,0,0}};
int H_in[6][3] = {{1,0,1},{1,0,0},{1,1,0},{0,1,0},{0,1,1},{0,0,1}};

//***********************************************************************
//***********************************************************************
//***********************************************************************
void setup() {
  pinMode(vel, OUTPUT);
  pinMode(dir, INPUT);
  pinMode(sA, INPUT);
  pinMode(sB, INPUT);
  pinMode(sC, INPUT);
  pinMode(Q0, OUTPUT);
  pinMode(Q1, OUTPUT);
  pinMode(Q2, OUTPUT);
  pinMode(Q3, OUTPUT);
  pinMode(Q4, OUTPUT);
  pinMode(Q5, OUTPUT);
  //Serial.begin(115200);
  analogWrite(vel,0);
  delay(1000);
}
//***********************************************************************
//***********************************************************************
//***********************************************************************
void loop() {
  int v_read = analogRead(A0);
  int Dv = int(255.0*((v_read-8.0)/1015.0));//<<<<<<<<<<<<<<
  if (Dv>255){Dv=255;}
  if (Dv<7){Dv=0;}
  analogWrite(vel,Dv);
  
  int D = digitalRead(dir);
  int v[3] = {digitalRead(sA),digitalRead(sB),digitalRead(sC)};
  for (int i = 0 ; i < 3 ; i++){
    v[i] = D^v[i];
    //Serial.print(v[i]);
  }
  if (v[0]==1 && v[1]==0 && v[2]==1){output(0);}
  else if(v[0]==1 && v[1]==0 && v[2]==0){output(1);}
  else if(v[0]==1 && v[1]==1 && v[2]==0){output(2);}
  else if(v[0]==0 && v[1]==1 && v[2]==0){output(3);}
  else if(v[0]==0 && v[1]==1 && v[2]==1){output(4);}
  else if(v[0]==0 && v[1]==0 && v[2]==1){output(5);}
  else {output(6);}  
  //Serial.println("*");
  //delay(1);
  delayMicroseconds(3);
}
//***********************************************************************
//***********************************************************************
//***********************************************************************
void output(int j){
  for (int k = 0 ; k < 6 ; k++){
    digitalWrite(k+5,bool(Q_out[j][k]));
    //Serial.print(Q_out[j][k]);
  }
}
