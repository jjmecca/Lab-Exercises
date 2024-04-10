import requests
import json
from tkinter import *
from base64 import b64encode

root = Tk()
root.geometry("570x500") 
root.title("Spotify App")

id = StringVar()
id.set("")

client_id = 'f917844e19fc44e1a42e6d76900b73c5'
client_secret = 'f71978d0529f4914942241811148b687'

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()

auth_data = {
    'grant_type': 'client_credentials'
}

auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)

#Now we can try requesting information
headers = {
    "Authorization": "Bearer " + token
}

def insert_text(text):
    text.insert(END, text)

def clear_text():
    text.delete("1.0", "end")
    
def artist_info(id):
    clear_text()
    response=requests.get(f"https://api.spotify.com/v1/artists/{id}/top-tracks?country=US",headers=headers)
    data=response.json()
    followers=data['followers']['total']
    name=data['name']
    popularity=data['popularity']
    genre=data['genres']
    insert_text(f"Name: {name}\nFollowers: {followers}\nGenre(s): {genre}\nPopularity Level: {popularity}")

entry_frame = Frame(root)
entry_frame.grid(row=0, column=0)
drop_frame = Frame(root)
drop_frame.grid(row=0, column=1)

label = Label(entry_frame , text="Enter Artist ID").pack()
entry = Entry(entry_frame , width=35, borderwidth=5, textvariable=id).pack()
button = Button(entry_frame , font = 24, text = "Get Information", command=lambda: artist_info(id.get()))
button.pack(pady = 20)
text = Text(root, height=16)
text.grid(columnspan=2)

button2 = Button(root, font = 24, text = "Close Window", 
                command=root.destroy)
button2.grid(columnspan=2, pady = 20)

root.mainloop()