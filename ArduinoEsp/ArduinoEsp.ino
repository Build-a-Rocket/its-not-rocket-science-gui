// PLEASE NOTE I did not touch the camera code!! I just did the sensor data code

//Include Libraries
#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include "radio_helpers.h"
#include "Adafruit_BMP3XX.h"
#include "camera_interface.h"
#include "Adafruit_LSM6DSOX.h"

// I2C Pins
#define I2C_SCL 2 // clock signal
#define I2C_SDA 4 // data bidirectional
 
// nRF24 Pins
#define NRF24_SCLK 14 // out green
#define NRF24_MISO 13 // in  purple
#define NRF24_MOSI 12 // out blue
#define NRF24_CS   15 // out orange
#define NRF24_CE   16 // 3.3 yellow (not used)
 
// nRF24 Values
#define RF24_CHANNEL 111 // Change this to your team's channel
 
SPIClass SPI2(VSPI);
RF24 radio(NRF24_CE, NRF24_CS);
 
//address through which two modules communicate.
const uint8_t txa[5] = {0x01, 0x00, 0x00, 0x00, 0x00};
const uint8_t rxa[5] = {0x02, 0x00, 0x00, 0x00, 0x00};
 
// bmp stuff
#define SEALEVEL_HPA 1013.25
Adafruit_BMP3XX bmp;
 // lsm6d
Adafruit_LSM6DSOX sox;

//image frame to send
byte *frame;
void setup()
{
  SPI2.begin(NRF24_SCLK, NRF24_MISO, NRF24_MOSI, NRF24_CS);
 
  Serial.begin(115200);
 
  if (!radio.begin(&SPI2))
  {
    Serial.println("Failed to start radio...");
  } else
  {
    Serial.println("Success!");
  }
 
  if (!radio.isChipConnected())
  {
    Serial.println("Failed to detect radio");
  } else
  {
    Serial.println("Success!");
  }
 
  if (!radio.isValid())
  {
    Serial.println("Failed?? Not a real radio??");
  } else
  {
    Serial.println("Success!");
  }
 

  
  radio.powerUp();
 
  // configure radio
  radio.openWritingPipe(rxa);
  radio.setDataRate(RF24_2MBPS);
  radio.setCRCLength(RF24_CRC_16);
  radio.setPALevel(RF24_PA_MAX);
  radio.enableDynamicPayloads();
  radio.enableAckPayload();
  radio.setChannel(RF24_CHANNEL);
  radio.stopListening();
 
  RadioHelpers::setRadio(radio);
  RadioHelpers::writeMessage("Radio Initialized");
 
  Wire.begin(I2C_SDA, I2C_SCL);
 
  while (!bmp.begin_I2C())
  {
    Serial.println("Failed to find the BMP388");
    RadioHelpers::writeMessage("Failed to find the BMP388");
    delay(1000);
  }
 
  Serial.println("Found BMP388");
  RadioHelpers::writeMessage("Found BMP388");
 
    // Set up oversampling and filter initialization
  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  bmp.setOutputDataRate(BMP3_ODR_50_HZ);

  while (!sox.begin_I2C())
  {
    Serial.println("Failed to find LSM6D");
     RadioHelpers::writeMessage("Failed to find LSM6D");
    delay(500);
  }
  
  Serial.println("Found LSM6D");
  RadioHelpers::writeMessage("Found LSM6D");
  // setup IMU
  sox.setAccelRange(LSM6DS_ACCEL_RANGE_16_G);
  sox.setGyroRange(LSM6DS_GYRO_RANGE_125_DPS);
  sox.setAccelDataRate(LSM6DS_RATE_12_5_HZ);
  sox.setGyroDataRate(LSM6DS_RATE_12_5_HZ);

  ESP_CAMERA::init_camera();
  frame = (byte *)malloc(10000);
  // Serial.end();

  RadioHelpers::writeMessage("Camera Initialized");

  Serial.println("Setup Complete");
  RadioHelpers::writeMessage("Setup Complete");
  delay(50);
}
 
void loop()
{ 
  bmp.performReading();
  
  // imu events
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  sox.getEvent(&accel, &gyro, &temp);
 
  double altitude = bmp.readAltitude(SEALEVEL_HPA);
  double temperature = bmp.temperature;
 
  String telemetry = "START,";
  telemetry += String(millis()) + ",";
  telemetry += String(altitude) + ",";
  telemetry += String(temperature) + ",";
  telemetry += String(gyro.gyro.x) + ",";
  telemetry += String(gyro.gyro.y) + ",";
  telemetry += String(gyro.gyro.z) + ",";
  telemetry += String(accel.acceleration.x) + ",";
  telemetry += String(accel.acceleration.y) + ",";
  telemetry += String(accel.acceleration.z) + ",";
  telemetry += "END\n";
  Serial.println("sent: " + telemetry);
  RadioHelpers::writeMessage(telemetry);
  
  int bytes = ESP_CAMERA::get_frame(frame);
  if (bytes > 0)
  {
   Serial.println("sent: " + bytes);
   RadioHelpers::writeBytes(frame, bytes);
  }
}