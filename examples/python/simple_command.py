"""
Example script to control eV-Technologies EVT3064 and EVT1064 Correlators
Date 19/11/2021
Licence MIT
"""

import serial

# First connect the device to the computer
# You can list available ports the the following command: "python -m serial.tools.list_ports"
# The default configuration is: 9600, 8, N, 1,no timeout, we could specify but configuring the baudrate is enough
correlator = serial.Serial('COM9', 100000)

# Send the command "S101" to connect the common port 1 to the input/output port 1
correlator.write(b"\S101")
# Send the command "S101" to connect the common port 1 to the input/output port 63
correlator.write(b"\S163")
# Send the command "S101" to connect the common port 2 to the input/output port 2
correlator.write(b"\S202")
# Send the command "S101" to connect the common port 2 to the input/output port 64
correlator.write(b"\S264")

# Close the connection
fem.close()
