
#* Importing all Operational files from the Program directory

from Programs import archiveurl
from Programs import ipadd
from Programs import header
from Programs import dns_mx_record
from Programs import portscan
from Programs import whoisdetail
from Programs import Subdomain
from Programs import ssl_info
from Programs import files

#* Importing Modules form Python 

import socket
import ssl
import requests
import subprocess
import requests
import re
from urllib.request import ssl
from urllib.request import socket
import datetime
import smtplib
import whois
from colorama import Fore
import threading



print("Welcome to Daemex Automation Reconnaissance Tool:\n")
print(r"""______            _     _  ______                 _           _ 


................................................................................
................................................................................
....:*%%%%*!.........**......!*%%%%%%:.:**........**!..!*%%%%%%::**......**.....
....:*#@@@@##$:.....$**%.....$*@@@@@$:.%**$......%**@..@*@@@@@$:.$*@...:&S*.....
....:*$.....*S#:...**%@*!....$*:.......%*@**....!*&*@..@*:........*S&:!S#:......
....:*@......!*%..:S#.:S#....$*%!!!!:..%*!&S:...#S:*@..@**!!!!:....!#SS@:.......
....:*@......:*@..@*!::**$...$*&&&&&%..%*!:S&..$*!:*@..@*&&&&&*....:&**$........
....:*@......@*!.%*#&&&&S**..$*:.......%*!.**%!*%.:*@..@*:........!#S!**@:......
....:*&!!!*$#S*.!*&::::::#S:.$**!!!!!:.%*!..$**&..:*@..@**!!!!!..*S&:..!S#!.....
....:&&&&&&@*:..$#:......!#%.%#&&&&&&:.*#!...@&:..:&%..%#&&&&&&:!&$.....:&@:....
................................................................................
................................................................................
................................................................................


                        """)
print("\n****************************************************************")
print("\n* Copyright of DAEMEX LLC, 2022                                *")
print("\n* https://www.daemex.io                                        *")
print("\n* Developed By: Sunil Kumar Gupta                              *")
print("\n****************************************************************")

print("\n")



Host=input("Enter Target Domain Name to Start Reconnaissance : >>\n")


ip= ipadd.ipaddress(Host)
header_info=header.Header(Host)
dnsrecoed=dns_mx_record.Dnsdetails(Host)
openports=portscan.portscan(Host)
SSL_Cert_Details=ssl_info.sslcert_info(Host)
whois_Details=whoisdetail.whois_info(Host)
subdomain_Data=Subdomain.Subdomain_enum(Host)
arch= archiveurl.archive(Host)
File=files.findfiles(Host)

print(ip)
print(header_info)
print(dnsrecoed)
print(openports)
print(SSL_Cert_Details)
print(whois_Details)
print(subdomain_Data)
print(arch)
print(File)
