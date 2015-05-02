from serial import Serial
from serial import SerialException
from threading import Timer
import time


MOVE_TIME = 5.0
SCAN_TIME = 2.0
DEVICE_ADDRESS = '/dev/ttyACM0'
BAUD_RATE = 9600

while True:
    try:
        print("Opening...")
        ser = Serial(DEVICE_ADDRESS, BAUD_RATE)
        break

    except SerialException:
        print("No device attached")


def scan():
    print("Scanning...")
    timeout = time.time() + SCAN_TIME

    while time.time() < timeout:
        a=2    # Some code I havent thought of yet
    print(time.strftime("%H:%M:%S"))
    print("Sending resume command.")
    ser.write(b'r')  # Command to tell the robot to resume
    init_timer()
    


def send_stop_command():
    print(time.strftime("%H:%M:%S"))
    print("Sending stop command.")
    ser.write(b's')  # Command to tell the robot to stop
    scan()


def init_timer():
    print(time.strftime("%H:%M:%S"))
    Timer(MOVE_TIME, send_stop_command).start()

init_timer()


filename = time.strftime("%d-%m-%Y_%H:%M:%S") + ".txt"

while True:
    data = ser.readline()
    try:
        with open(filename, "ab") as outfile:
            outfile.write(data)
            outfile.close()
    except IOError:
        print("Data could not be written")
