int sensor_pin = A0;  // Signal from the capacitive soil moisture sensor
int output_value;      // Value of soil moisture
int pump = 3;          // Digital pin where the relay is plugged in
int threshold = 5;     // Threshold value to trigger pump

void setup() {
  Serial.begin(9600);
  pinMode(sensor_pin, INPUT);  // Setup for the soil moisture sensor
  pinMode(pump, OUTPUT);       // Setup for the pump
  Serial.println("Reading From the Sensor ...");
  delay(1000);                 // Initial delay
}

void loop() {
  output_value = analogRead(sensor_pin);                  // Get sensor value
  output_value = map(output_value, 550, 0, 0, 100);      // Map to percentage
  Serial.print("Moisture: ");
  Serial.print(output_value);                             
  Serial.println("%");
  delay(2000);               // Wait 10 seconds

  controlPump();              // Call pump control function
}

void controlPump() {
  if (output_value < threshold) {                         // Check if soil is dry
    digitalWrite(pump, HIGH);
    Serial.println("Pump on");
    delay(10000);        // Run pump for 1 second
    digitalWrite(pump, LOW);
    Serial.println("Pump off");
  } else {
    Serial.println("Soil is moist - pump off");
  }
  delay(2000); // Wait 5 minutes
}
