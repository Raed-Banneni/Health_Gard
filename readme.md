(The final and enhanced version of the firmware is in Healthgard_interrupt directory, Healthgard directory contains the old version that uses polling technique instead of interrupts)


HealthGuard is a wearable health monitoring device based on the STM32 Nucleo L476RG board, which is equipped with an MPU6050 accelerometer and gyroscope for fall detection, and a MAX30102 sensor for measuring heart rate and blood oxygen saturation levels (SpO2). The device is capable of detecting falls and alerting emergency contacts via the integrated ESP32 Wi-Fi module. HealthGuard also allows for seamless transfer of sensor data to a web application, which can be accessed by healthcare professionals for analysis and monitoring of patient health over time.

Ps : the Max_30102 code is writen by the contributer "Majd Khiari" designed for and compiled to run on the STM32 F4 microcontroller platform, we will merge the codes soon into only one firmware that runs on one of our boards (nucleo-l476rg or nucleo-f401re).
