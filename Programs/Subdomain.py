import requests
from colorama import Fore

def Subdomain_enum(Host):
    domain =Host

    file = open("Subdomains.txt")


    content = file.read()

    subdomains = content.splitlines()


    Found_subdomains = []
    for subdomain in subdomains:
    
        url = f"http://{subdomain}.{domain}"
        try:
        
            response = requests.get(url)
            if response.status_code==200:
                print(Fore.GREEN +f"Subdomain Found [+]: {url}")
                Found_subdomains.append(url)

        except requests.ConnectionError:
       
            pass

        # save the discovered subdomains into a file
        with open("Found_Subdomains.txt", "w") as f:
            for subdomain in Found_subdomains:
                print(subdomain, file=f)