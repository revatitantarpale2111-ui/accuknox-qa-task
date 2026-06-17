import requests

url=input('enter website URL:')

try:
    response=requests.get(url)

    if response.status_code==200:
        print('application status:UP')
    else:
        print('application status: DOWN')
        print('status code:',response.status_code)

except Exception as e:
    print('application status: DOWN')
    print('Error:',e)