void setup() {
  // start external serial port
  Serial1.begin(9600);
  Serial1.println("measurement over Logic Analyzer");
}

void loop() {
    delay(1000);
    Serial1.println("Test message");
}
