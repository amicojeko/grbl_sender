# grbl_sender
A simple python GRBL sender

usage: 

`grbl_sender [-h] -P PORT [-v] [-s SPEED] filename`

Sends GCODE via serial port.

positional arguments:
  
`filename` GCODE filename

optional arguments:

`-h, --help` 
show this help message and exit

`-P PORT` 
Serial port

`-v` 
verbose

`-s SPEED` 
Serial port speed, default is 115200bps
