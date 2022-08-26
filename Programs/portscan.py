
import socket
import re

open_ports = []

port_range = [1, 3, 4, 6, 7, 9, 13, 17, 19, 20, 21, 22, 23, 24, 25, 26, 30, 32, 33, 37, 42, 43, 49, 53, 70, 79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 99, 100, 106, 109, 110, 111, 113, 119, 125, 135, 139, 143, 144, 146, 161, 163, 179, 199, 211, 212, 222, 254, 255, 256, 259, 264, 280, 301, 306, 311, 340, 366, 389, 406, 407, 416, 417, 425, 427, 443, 444, 445, 458, 464, 465, 481, 497, 500]
port_min = int(port_range[0])
port_max = int(port_range[-1])

def portscan(Host):
    # Basic socket port scanning
    print("\n====================================================================\n")
    print(f'Following is the Port scan results of {Host} Domain:\n')
    Target_ip=socket.gethostbyname(Host)
    for port in range(port_min, port_max + 1):
    
        try:
        
                        
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
                s.settimeout(0.5)
           
                s.connect((Target_ip, port))
            
                open_ports.append(port)

        except:
        
            pass


    for port in open_ports:
   
        print(f"Port {port} is open on {Target_ip}.")
    