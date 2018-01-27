#!/usr/bin/env python
import serial
import time
import argparse

parser = argparse.ArgumentParser(description='Sends GCODE via selected serial.')

parser.add_argument("-P", help="Serial port", required=1, dest="port")
parser.add_argument("-v", help="verbose", dest="verbose", action='store_true')
parser.add_argument("-s", help="Serial port speed, default is 115200bps", dest="speed", default=115200, type=int)
parser.add_argument("filename", help="GCODE filename")

args        = parser.parse_args()
serial_port = serial.Serial(args.port, args.speed)
grbl_file   = open(args.filename,'r');

# GRBL Init sequence
serial_port.write("\r\n\r\n")
time.sleep(2)  
serial_port.flushInput() 

for line in grbl_file:
    l = line.strip() 
    if args.verbose: print 'Sending: ' + l,
    serial_port.write(l + '\n') 
    grbl_out = serial_port.readline()
    if args.verbose: print ' : ' + grbl_out.strip() # GRBL Response

grbl_file.close()
serial_port.close()    
