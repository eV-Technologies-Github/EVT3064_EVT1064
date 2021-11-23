"""
Example script to control eV-Technologies EVT3064 and EVT1064 Correlators
Date 19/11/2021
Licence MIT
"""

import serial
import time

def select_port(common, port):
    common_str = str(common)
    port_str = str(port)
    # Check if we must add a '0'
    if port < 10:
        return('S' + common_str + '0' + port_str)
    else:
        return('S' + common_str + port_str)

# First connect the device to the computer
# You can list available ports the the following command: "python -m serial.tools.list_ports"
# The default configuration is: 9600, 8, N, 1,no timeout, we could specify but configuring the baudrate is enough
correlator = serial.Serial('COM14', 100000)
#correlator.open()

# EVT3064 and EVT1064 have 2 common ports and 64 input/output ports
nb_common_ports = 2
nb_ports = 64
Delay = 100 # in milliseconds

# Demo function that switch sequentially all the ports (firts the port 1 access to all the ports then the port 2)
def demo_mode():
    for common in range (1, nb_common_ports+1): # Python range end with the -1 index
        for port in range(1, nb_ports+1):
            data_to_send = select_port(common, port)
            # Variable to be sent has to be an ASCII string
            correlator.write(data_to_send.encode('ascii'))
            print("Command sent: ", data_to_send)
            # Delay in seconds
            time.sleep(Delay/1000)

demo_mode()

correlator.close()
