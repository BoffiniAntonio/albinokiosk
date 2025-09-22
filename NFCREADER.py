import serial

ser = serial.Serial('COM5', 9600, timeout=1)

print("Listening for NFC UID...")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print("Received from Arduino:", line)
