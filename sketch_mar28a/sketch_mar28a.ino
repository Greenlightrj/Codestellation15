#include <Servo.h>

Servo myservo;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600); //baud rate
  myservo.attach(9);
}

void servo_out (Servo servo, char input) {
  if (input == 'a') {
    servo.write(10);
  } else if (input == 'b') {
    servo.write(40);
  } else if (input == 'c') {
    servo.write(70);
  } else if (input == 'd') {
    servo.write(100);
  } else if (input == 'e') {
    servo.write(130);
  } else if (input == 'f') {
    servo.write(150);
  }
}
    

// the loop routine runs over and over again forever:
void loop() {
  char inByte = ' ';
  if (Serial.available()) {
    inByte = Serial.read();
    Serial.println(inByte);
    servo_out(myservo, inByte);
  }
  
}  // turn the LED off by making the voltage LOW}
