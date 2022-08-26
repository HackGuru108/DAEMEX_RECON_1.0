#!/usr/bin/env python3


import subprocess

#getting the mail server Records
def Dnsdetails(Host):
    print("\n====================================================================\n")
    print("\n[+] The Mail Sever Records are: [+]")
    subprocess.call(["host", "-t", "mx",Host])
    print()
    print("\n====================================================================\n")

#getting the name server records


    print("[+] The Name Server Records are: [+]")
    subprocess.call(["nslookup",Host])
    print()
    