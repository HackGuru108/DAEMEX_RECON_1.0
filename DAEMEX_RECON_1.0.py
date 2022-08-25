
from Programs import archiveurl
from Programs import ipadd
from Programs import header
from Programs import dns_mx_record
from Programs import portscan
from Programs import whoisdetail
from Programs import Subdomain
from Programs import ssl_info

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
from Programs.ssl_info import sslcert_info


print("Welcome to Daemex Automation Reconnaissance Tool:\n")
print(r"""______            _     _  ______                 _           _ 


				   SS        #S
		    #####	  #&&#       &###
	          S &&##@S	S&&###&S     #SS#&S
	     #&###@ &&&#@S     #@######&S     SSSS&S
	     #&###&  SSSS     &&###@&###&&     #SSS#S
	     #&&&&&   &######&&##&&S &&###&     &#SS#&
	              &#########&&    ###S#&#    &#SSS&S
	      #&###& S&########@&    &&###SS&#    #&SSS##
	      @&###@ S&#######&#   S@&###&#SS#@S   S&SSS#S
	      @&#&#@  &#######&#  #@###&&S&&SS#@S    &#SSS&
	        S      SSS#SSSSS  &@###@#   &&SSS&&    #&SSS#S
		SSSSS   SSS    &&###&S     S@#SS#@S   #&SSS#S
		@&&&@#  @&#@S  #&####         @#SS##    #SS S#
	       #@###&#  #&##   #@###&&       &&SSS&#    ##S S#S
	       #@&&&@# #S###S   S@&##&@     @&SS#@S   #&SSSS#
		       S&###@#    @&###@S S&#SS#&S   #@SSS##
			#@###&&    #@###&&@#SS&#    &&SSS&S
			 S&&##&&S   S&####SS#&S   S@#SS#@S
			   &&###@S    &&##S##    #@#SS#&
			    #@###@#    #&#S#@#  #&SSS&S
			     S@&##&##&  S&#SS&#&#SSS&S
			       &&#####@S  &#SS##SS##
				#&####&#   &&SSSS#S
				 S&##&S     S&#S#
                                   ##S        ##

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

arch= archiveurl.archive(Host)
ip= ipadd.ipaddress(Host)
header_info=header.Header(Host)
dnsrecoed=dns_mx_record.Dnsdetails(Host)
openports=portscan.portscan(Host)
SSL_Cert_Details=ssl_info.sslcert_info(Host)
whois_Details=whoisdetail.whois_info(Host)
subdomain_Data=Subdomain.Subdomain_enum(Host)

print(dnsrecoed)
print(ip)
print(arch)
print(header_info)
print(openports)
print(SSL_Cert_Details)
print(whois_Details)
print(subdomain_Data)
