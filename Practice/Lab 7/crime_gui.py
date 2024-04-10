import requests
import json
from tkinter import *

root = Tk()
root.geometry("570x500") 
root.title("Crime App")
state="NY"
api_key = "722b890b45572aeadcad24099d59c8903f685ae9"
url = f"https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:{state}&key={api_key}"

json_file = requests.get(url).json()

print(json_file)

root.mainloop()