#this is taken from the spotify documentation
#base 64 allows us to encode our string
import requests
from base64 import b64encode

client_id = 'f917844e19fc44e1a42e6d76900b73c5'
client_secret = 'f71978d0529f4914942241811148b687'

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()

auth_data = {
    'grant_type': 'client_credentials'
}

#we are POSTING something to the server in order to RETURN the token
auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)

#Now we can try requesting information
artist_id = "4Uc8Dsxct0oMqx0P6i60ea?si=QvwSF7bOToiljHRHLd-uqQ"
url = f"https://api.spotify.com/v1/artists/{artist_id}"
ids='5hIOd0FvjlgG4uLjXHkFWI?si=5RDtl2i1R3CgFnTONvk-lg','2CMlkzFI2oDAy5MbyV7OV5?si=_8RDrRaBQoy4Kh0ZgvJ8tw'
albums_url = f"https://api.spotify.com/v1/albums/{ids[0]}"
albums_url2 = f"https://api.spotify.com/v1/albums/{ids[1]}"
headers = {
    "Authorization": "Bearer " + token
}

response = requests.get(url, headers=headers)
response2 = requests.get(albums_url, headers=headers)
response3 = requests.get(albums_url2, headers=headers)
data = response.json()
album_data= response2.json()
album_data2= response3.json()
print(data['name']+": "+album_data['name']+", "+album_data2['name'])
