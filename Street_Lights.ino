/*
  Button

 Turns on and off a light emitting diode(LED) connected to digital
 pin 13, when pressing a pushbutton attached to pin 2.


 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground

 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.


 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Button
 */

// constants won't change. They're used here to
// set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin
int GreenLED = 10 ;
int RedLED = 12 ;
int YellowLED = 11 ;
int PedGLED = 9 ;
int PedRLED = 8 ;
// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  pinMode(RedLED, OUTPUT);
  pinMode(YellowLED, OUTPUT);
  pinMode(GreenLED,OUTPUT);
  digitalWrite(GreenLED,HIGH);
  digitalWrite(PedRLED,HIGH);
  pinMode(PedGLED,OUTPUT);
  pinMode(PedRLED,OUTPUT);

}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
       digitalWrite(GreenLED, LOW);   // turn the LED on (HIGH is the voltage level)             // wait for a second
      digitalWrite(YellowLED,HIGH);    // turn the LED off by making the voltage LOW
      delay(5000);              // wait for a second
      digitalWrite(YellowLED, LOW);    // turn the LED off by making the voltage LOW
      digitalWrite(RedLED, HIGH);   // turn the LED on (HIGH is the voltage level
      digitalWrite(PedRLED,LOW);
      delay(1000);
      digitalWrite(PedGLED, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(7000);
      digitalWrite(PedGLED, HIGH);   // turn the LED on (HIGH is the voltage level)
      digitalWrite(RedLED,LOW);   // turn the LED on (HIGH is the voltage level)
      digitalWrite(PedGLED,LOW);
      digitalWrite(GreenLED,HIGH);
      digitalWrite(PedRLED,HIGH);

