import ipaddress 
from constants import *

def validate_ip(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address)) 


def validate_port(port):
    # type: (str) -> bool
    cond1 = port.isdigit()          
    cond2 = (1 <= int(port) <= 65535)
    try:
        if cond1 and cond2:
            print("This is a VALID port number.")
            return True
    except ValueError:
        print("This is NOT a valid port number.")
        return False
    print("This is NOT a valid port number.")
    return False

def validate_ip_port(PORT, HOST):
    RETURN_HOST = HOST
    RETURN_PORT = PORT
    IP_VALIDATION = False
    PORT_VALIDATION = False
    if HOST == "0":
        IP_VALIDATION = True
        RETURN_HOST = HOST
    else:
        IP_VALIDATION = validate_ip(HOST)
    PORT_VALIDATION = validate_port(PORT)
    if IP_VALIDATION and PORT_VALIDATION:
        return True, RETURN_HOST, RETURN_PORT
    else:
        return False, None, None