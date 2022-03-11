""" Envio de la Lectura de sensores ACTIVE BRO"""

from GetPulse import GetPulse
from mpu6050 import mpu6050
import time
import requests

mpu = mpu6050(0x68)
p = GetPulse()
p.startAsyncBPM()

while True:
    
    bpm = p.BPM
    acel_data = mpu.get_accel_data()
    print("Acc X : "+str(round(acel_data['x'],3)))
    print("Acc Y : "+str(round(acel_data['y'],3)))
    print("Acc Z : "+str(round(acel_data['z'],3)))
    print()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(round(gyro_data['x'],3)))
    print("Gyro Y : "+str(round(gyro_data['y'],3)))
    print("Gyro Z : "+str(round(gyro_data['z'],3)))
    print()
    print("-------------------------------")
    
    
    if bpm > 0:
        
        print("BPM: %d" % bpm)
    else:
        print("No Heartbeat detected")
        
    envio = requests.get("https://api.thingspeak.com/update?api_key=NLCJHRS7IXQKW30Y&field1="+str(bpm))
    
    time.sleep(1)
