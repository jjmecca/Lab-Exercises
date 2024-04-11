import requests
import json
from tkinter import *

root = Tk()
root.geometry("580x500") 
root.title("Weather App")

lat = StringVar() # lat = "42.098701"
lat.set("")
lon = StringVar() # lon = "-75.912537"
lon.set("")
city_select = StringVar()
city_select.set("Select a City")

#source https://forecast.weather.gov/stations.php?foo=0
city_list = ["Binghamton", "New York", "Chicago", "Atlanta", "Denver"]

#list syntax: [lat, lon]
city_latlon = {"Binghamton": ["42.09", "-75.91"],
               "New York": ["40.78", "-73.96"],
              "Chicago": ["41.98", "-87.9"],
              "Atlanta": ["33.66", "-84.42"],
              "Denver": ["39.87", "-104.67"]}

#This function deletes the text that is already in the textbox and inserts the new text containing information about the whether forecast
def weekly_forecast(lat, lon, option=None):
    weather_text.delete("1.0", "end")
    weather_text.insert(END, f"Weather for {option} \n\n")
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    json = weather.json()
    forecast = json["properties"]["forecast"]
    daily_forecast = requests.get(forecast).json()

    for section in daily_forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        #I changed the text here to make it look a little nicer
        text = f"{day}: {temp} \n\n"
        weather_text.insert(END, text)
        weather_text.tag_config("tag_name", justify="center")
        weather_text.tag_add("tag_name", "1.0", "end")

#This function is connected to the Select City button.
#This simply selects the city that is chosen in the list and then uses the weekly_forecast function.
def chosen_option():
    option = city_select.get()
    value = city_latlon[option]
    lat = value[0]
    lon = value[1]
    weekly_forecast(lat,lon, option)

entry_frame = Frame(root) #This is used for organization
entry_frame.grid(row=0, column=0)
drop_frame = Frame(root) #This is used for organization
drop_frame.grid(row=0, column=1)

label_lat = Label(entry_frame , text="Enter Latitude").pack() #This is just text
entry_lat = Entry(entry_frame , width=35, borderwidth=5, textvariable=lat).pack() #This is where you enter latitude, this connects to the lat variable
label_lon = Label(entry_frame , text="Enter Longitude").pack() #This is just text
entry_lon = Entry(entry_frame , width=35, borderwidth=5, textvariable=lon).pack() #This is where you enter longitude, this connects to the lon variable
button = Button(entry_frame , font = 24, text = "Get Forecast", 
                command=lambda: weekly_forecast(lat.get(), lon.get())) #This button gets the forecast from the written longitude and latitudes and uses the weekly_forecast function
button.pack(pady = 20)

drop_label = Label(drop_frame, text="You can also select a city:").pack() #This is just text
dropdown = OptionMenu(drop_frame, city_select, *city_list).pack() #This is a dropdown of some cities to select from
choose_button = Button(drop_frame, text="Select City", command=chosen_option) #This is a button to select a city and forwards to the chosen_option function
choose_button.pack(pady = 20)

#I added a scrollbar to scroll through the text
scrollbar=Scrollbar(root) #This creates a scrollbar
weather_text = Text(root, height=16,yscrollcommand=scrollbar.set) #This creates a textbox connected to a scrollbar to insert the forecast text
weather_text.grid(columnspan=2)
scrollbar.config(command=weather_text.yview)
scrollbar.grid(row=1, column=2, rowspan=1, sticky="ns")

button2 = Button(root, font = 24, text = "Close Window", 
                command=root.destroy) #This is a close button that simply destroys the window
button2.grid(columnspan=2, pady = 20)

root.mainloop()