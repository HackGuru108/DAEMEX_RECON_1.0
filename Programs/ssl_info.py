


from urllib.request import ssl, socket

import datetime, smtplib



def sslcert_info(Host):
    hostname = Host
    port = '443'


    context = ssl.create_default_context()


    with socket.create_connection((hostname, port)) as sock:

        with context.wrap_socket(sock, server_hostname = hostname) as ssock:

            certificate = ssock.getpeercert()
    print("\n====================================================================\n")
    print(f'Following is SSL_CERTIFICATE Information of {Host} \n')
    print(certificate)
    