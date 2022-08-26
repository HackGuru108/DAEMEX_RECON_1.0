import requests
  
def Header(Host):
    Host1 = f"https://{Host}"
    response = requests.get(Host1)

    print("\n====================================================================\n")
    print(f'Header Information of {Host1} is as Follows: \n' )
  
    print(response)
    print(response.headers)
    



