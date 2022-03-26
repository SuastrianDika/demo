// Contoh penggunaan Bidrige untuk WSN
// Sketch WeMos pertama

#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "Token Anda";
char ssid[] = "Nama Wifi Anda";
char pass[] = "Password Wifi Anda";

BLYNK_WRITE(V2) { //LED Hijau
  int pinData = param.asInt();
}

BLYNK_WRITE(V3){ //LED Merah
  int pinData = param.asInt();
}

void setup(){
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
}

void loop(){
  Blynk.run();
}