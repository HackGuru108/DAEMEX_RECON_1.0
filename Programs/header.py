import requests
  



def Header(Host):
    response = requests.get('https://codesprout.in')
  

    print(response)
    print(response.headers)


