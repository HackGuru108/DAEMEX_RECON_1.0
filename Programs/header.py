import requests
  



def Header(Host):
    response = requests.get(Host)
  

    print(response)
    print(response.headers)


