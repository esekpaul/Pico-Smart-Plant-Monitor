# 🌿 Smart Plant Monitor with Raspberry Pi Pico

An advanced environmental monitoring system that tracks light intensity and temperature to ensure optimal conditions for indoor plants.

## 🚀 Key Features
- **Real-time Light Meter:** Maps ambient light levels to a 10-segment LED bar.
- **Visual & Serial Alerts:** Sends a notification to the shell when light reaches maximum capacity.
- **Thermal Safety Alarm:** An active buzzer triggers a warning beep if the temperature exceeds a safety threshold.
- **ADC Signal Processing:** Uses voltage dividers to read analog data from LDR and NTC Thermistor sensors.

## 📺 Video Demo
Click the image below to watch the system in action:

[![Watch the video](https://img.youtube.com/vi/pqKJtCltroM/maxresdefault.jpg)](https://youtube.com/shorts/pqKJtCltroM)

## 🛠️ Components Used
- **Microcontroller:** Raspberry Pi Pico (RP2040)
- **Display:** 10-segment LED Bar
- **Sensors:** Photoresistor (LDR) & NTC Thermistor (10k)
- **Sound:** Active Buzzer
- **Resistors:** 10x 220Ω (Current limiting), 2x 10kΩ (Voltage dividers)

---
*Developed as part of my embedded systems learning journey.*
