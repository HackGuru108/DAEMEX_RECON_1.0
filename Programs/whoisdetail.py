import whois



def whois_info(Host):
    domain_name = Host
    whois_info = whois.whois(domain_name)
    print("\n====================================================================\n")
    print(f'Following is the whois information of {Host}\n')

    print(whois_info)

    