import whois



def whois_info(Host):
    domain_name = Host
    whois_info = whois.whois(domain_name)

    print(whois_info)