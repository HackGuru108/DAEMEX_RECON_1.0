
import socket

def ipaddress(Host):
    Target_ip=socket.gethostbyname(Host)

    print("\n====================================================================\n")
    print(f"\n Public IP Address of the {Host} is {Target_ip} ")

   


