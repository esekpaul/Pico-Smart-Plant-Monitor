from machine import Pin, ADC
import time

lumina_sensor = ADC(Pin(27))
temp_sensor = ADC(Pin(28))
buzzer = Pin(16, Pin.OUT)
pini_led = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
leduri = [Pin(p, Pin.OUT) for p in pini_led]

print("Smart Plant Monitor pornit!")

while True:
    val_L = lumina_sensor.read_u16()
    val_T = temp_sensor.read_u16()
    
    nr_leduri = int((val_L / 15000) * 10)
    if nr_leduri > 10: nr_leduri = 10
    
    if nr_leduri == 10:
        print("Lumina este la nivel maxim!")
    
    for i in range(10):
        leduri[i].value(1 if i < nr_leduri else 0)
    
    if val_T > 35000:
        print(f"Alarma Caldura! Valoare: {val_T}")
        buzzer.value(1)
        time.sleep(0.1)
        buzzer.value(0)
    
    time.sleep(0.2)
