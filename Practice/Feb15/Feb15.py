import json
import csv
import requests
import pandas as pd
API_key="5c5f66f994556e8f85ab7c9714a14b745210b8fe"
ny_url=f"https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:01&key={API_key}"

census_data=requests.get(ny_url)
json_file=census_data.json()

print(json_file)