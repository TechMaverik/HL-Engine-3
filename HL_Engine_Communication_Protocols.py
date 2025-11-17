"""
HL_Engine_Communication_Protocols.py
Author:Akhil P Jacob
HLDynamic-Integrations
"""
import serial
import smtplib
import os
import time
import bluetooth  # Linux Systems Only
from HL_CommonDependency import *


class CommunicationProtocolsEngine:
    """Communication Protocol Engine"""

    def find_Port(self):
        """automatically connect to serial port"""
        try:
            ser = serial.Serial("COM1", BAUD_RATE)
            display_message("Connected to COM1")
            return "COM1"
        except:
            display_message("Disconnected to COM1")

        try:
            ser = serial.Serial("COM2", BAUD_RATE)
            display_message("Connected to COM2")
            return "COM2"
        except:
            display_message("Disconnected to COM2")

        try:
            ser = serial.Serial("COM3", BAUD_RATE)
            display_message("Connected to COM3")
            return "COM3"
        except:
            display_message("Disconnected to COM3")

        try:
            ser = serial.Serial("COM4", BAUD_RATE)
            display_message("Connected to COM4")
            return "COM4"
        except:
            display_message("Disconnected to COM4")

        try:
            ser = serial.Serial("COM5", BAUD_RATE)
            display_message("Connected to COM5")
            return "COM5"
        except:
            display_message("Disconnected to COM5")

        try:
            ser = serial.Serial("COM6", BAUD_RATE)
            display_message("Connected to COM6")
            return "COM6"
        except:
            display_message("Disconnected to COM6")

        try:
            ser = serial.Serial("COM7", BAUD_RATE)
            display_message("Connected to COM7")
            return "COM7"
        except:
            display_message("Disconnected to COM7")

        try:
            ser = serial.Serial("COM8", BAUD_RATE)
            display_message("Connected to COM8")
            return "COM8"
        except:
            display_message("Disconnected to COM8")

        try:
            ser = serial.Serial("COM9", BAUD_RATE)
            display_message("Connected to COM9")
            return "COM9"
        except:
            display_message("Disconnected to COM9")

        try:
            ser = serial.Serial("COM10", BAUD_RATE)
            display_message("Connected to COM10")
            return "COM10"
        except:
            display_message("Disconnected to COM10")

        try:
            ser = serial.Serial("COM11", BAUD_RATE)
            display_message("Connected to COM11")
            return "COM11"
        except:
            display_message("Disconnected to COM11")

        try:
            ser = serial.Serial("COM12", BAUD_RATE)
            display_message("Connected to COM12")
            return "COM12"
        except:
            display_message("Disconnected to COM12")

        try:
            ser = serial.Serial("COM13", BAUD_RATE)
            display_message("Connected to COM13")
            return "COM13"
        except:
            display_message("Disconnected to COM13")

        try:
            ser = serial.Serial("COM14", BAUD_RATE)
            display_message("Connected to COM14")
            return "COM14"
        except:
            display_message("Disconnected to COM14")

        try:
            ser = serial.Serial("COM15", BAUD_RATE)
            display_message("Connected to COM15")
            return "COM15"
        except:
            display_message("Disconnected to COM15")

        try:
            ser = serial.Serial("COM16", BAUD_RATE)
            display_message("Connected to COM16")
            return "COM16"
        except:
            display_message("Disconnected to COM16")

        try:
            ser = serial.Serial("COM17", BAUD_RATE)
            display_message("Connected to COM17")
            return "COM17"
        except:
            display_message("Disconnected to COM17")

        try:
            ser = serial.Serial("COM18", BAUD_RATE)
            display_message("Connected to COM18")
            return "COM18"
        except:
            display_message("Disconnected to COM18")

        try:
            ser = serial.Serial("COM19", BAUD_RATE)
            display_message("Connected to COM19")
            return "COM19"
        except:
            display_message("Disconnected to COM19")

        try:
            ser = serial.Serial("COM20", BAUD_RATE)
            display_message("Connected to COM20")
            return "COM20"
        except:
            display_message("Disconnected to COM20")

        try:
            ser = serial.Serial("/dev/ttyUSB0", BAUD_RATE)
            display_message("Connected to /dev/ttyUSB0")
            return "/dev/ttyUSB0"
        except:
            display_message("Disconnected to /dev/ttyUSB0")

        try:
            ser = serial.Serial("/dev/ttyACM0", BAUD_RATE)
            display_message("Connected to /dev/ttyACM0")
            return "/dev/ttyACM0"
        except:
            display_message("Disconnected to /dev/ttyACM0")

    def ser_send(self, port, rate, data):
        """Send data to serial port"""
        try:
            ser = serial.Serial(port, rate)
            time.sleep(2)
            ser.write(str.encode(str(data)))
            return "HLEngine:data sent..."
        except:
            return False

    def ser_receive(self, port, rate):
        """Receive data from serial port"""
        try:
            ser = serial.Serial(port, rate)
            Serial_data = ser.readline()
            return Serial_data
        except:
            return False

    def shutDown_windows(self):
        """Shutdown windows system"""
        try:
            os.system("shutdown /s /t 1")
        except:
            return False

    def reboot_windows(self):
        """Reboot windows system"""
        try:
            os.system("restart /s /t 1")
        except:
            return False

    def linux_shutdown(self):
        """Shutdown linux system"""
        try:
            os.system("poweroff")
        except:
            return False

    def linux_boot(self):
        """Reboot linux System"""
        try:
            os.system("reboot")
        except:
            return False

    def botAccess(self, bot_address):
        """Connect to BT Device using Linux"""
        try:
            bd_addr = bot_address
            port = 1
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((bd_addr, port))
            display_message("Connection to BT device [established]")
            while 1:
                to_send = input("Enter your wireless command here:  ")
                if to_send != "exit":
                    sock.send(to_send)
                elif to_send == "exit":
                    break
        except:
            return False
