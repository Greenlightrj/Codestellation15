"""
codestellation whoop whoop
trying to get python and arduino to interact with serial!
either
$
serial
sg0
sg1
ttyACM0




"""

import time
import serial
# import io

# from face_reader import *

ser = serial.Serial('/dev/ttyACM1', 9600) #port and baud. pretty sure it's ttyACM0
# sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# for letter in ['a','b','c','d','e','f']:
#     ser.write(str(chr(ord(letter))))
#     time.sleep(5)

while True:
    ser.write(str(chr(97)))
    time.sleep(2)
    # sio.flush()
    ser.write(str(chr(98)))
    time.sleep(2)
    # sio.flush()
# while True:
#     # counter += 1
#     ser.write(str(chr(ord(letter))))
#     print(letter)
#     print(str(chr(ord(letter))))
#     time.sleep(5)
#     # ser.write(counter) #convert number to ascii
#     # print ser.readline() #reads any output from the arduino
#     # if counter == 64:
#     #     counter = 32
#     # time.sleep(.1)