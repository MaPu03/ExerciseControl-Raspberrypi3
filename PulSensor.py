from GetPulse import Getpulse
import time

p = HeartBeat()
p.startAsyncBPM()

try:
    while True:
        bpm = p.BPM
        if bpm > 0:
            print("BPM: %d" % bpm)
        else:
            print("No Heartbeat detected")
        time.sleep(1)
except:
    p.stopAsyncBPM()
