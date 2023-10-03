#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int T = 7;
int E =6;
int D1;
float D2 = 0;
int level = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup(){  
  lcd.begin(16,2);
  pinMode(T, OUTPUT);
  pinMode(E, INPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);

  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop(){
  digitalWrite(T, LOW);
  delay(9);
  digitalWrite(T, HIGH);
  delay(12);
  digitalWrite(T, LOW);
  
  D1 = pulseIn(E, HIGH);
  D2 = D1*0.0344/2;
  D2 = map(D2, 0, 344, 1000, 0);
  D2 = (D2/100);
  
 
  lcd.setCursor(0,0);
  if (D2 < 1){
    lcd.print("Normal           ");
    delay(12);
  }
  else if((D2>1)&&(D2<3)){
    lcd.print("Risk increasing  ");
    delay(12);
  }
  else{
    lcd.print("Danger           ");
    delay(12);
  }
   level = 0.01723 * readUltrasonicDistance(7, 6);
  if (level <= 240) {
    tone(8, 523, 1000); // play tone 60 (C5 = 523 Hz)
    Serial.println("Evacuate ");
    digitalWrite(10, HIGH);
    digitalWrite(9, LOW);
  }
  if (level > 240) {
    digitalWrite(10, LOW);
    digitalWrite(9, HIGH);
    Serial.println("Normal");
  }

  
  delay(12);
}