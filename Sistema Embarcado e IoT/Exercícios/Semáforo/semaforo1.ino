void setup(){
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);  
}
void loop(){
  for(int x = 3; x <= 5; x++){
    for(int y = 3; y <= 5; y++){
      if (x == y) {
      	digitalWrite(x, 1);
      	delay(1000);
      } else {
        digitalWrite(y, 0);
      }
    }
  }
  for(int x = 3; x <= 5; x++){
    digitalWrite(x, 0);
  }
}
  