const int limitSwitchPin = 32;

int buttonState;             
int lastButtonState = HIGH;   
unsigned long lastDebounceTime = 0;  
unsigned long debounceDelay = 50;    

void setup() {
  Serial.begin(115200);
  pinMode(limitSwitchPin, INPUT_PULLUP);
}

void loop() {
  int reading = digitalRead(limitSwitchPin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis(); 
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == LOW) {
        Serial.println("TRIGGER");
      }
    }
  }
  lastButtonState = reading;
}
