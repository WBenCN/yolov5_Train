import serial

serialPort = "COM3"
baudRate = 9600
ser = serial.Serial(serialPort, baudRate, timeout=0.5)

demo1=b"0"
demo2=b"1"
while 1:
    c=input('iput:')
    c=ord(c)
    if(c==48):
        ser.write(demo1)
    if(c==49):
        ser.write(demo2)