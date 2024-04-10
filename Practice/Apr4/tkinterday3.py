import requests
import json
from tkinter import *

root = Tk()
root.geometry("570x500") 
root.title("Weather App")

lat = StringVar()
lat.set("")
lon = StringVar()
lon.set("")

def insert_text(text):
    test_widget.insert(END, text)

def clear_text():
    test_widget.delete("1.0", "end")
    
def weekly_forecast(lat, lon):
    clear_text()
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    json = weather.json()
    forecast = json["properties"]["forecast"]
    daily_forecast = requests.get(forecast).json()

    for section in daily_forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        insert_text(f"{day}: {temp} \n")

def city_choice():
    choice=city_select.get()
    lat_lon=city_latlon[choice]
    lat.set(lat_lon[0])
    lon.set(lat_lon[1])
    weekly_forecast(lat.get(),lon.get())

city_select = StringVar()
city_select.set("Select a City")

city_list = ["Binghamton", "New York", "Chicago", "Atlanta", "Denver"]

city_latlon = {"Binghamton": ["42.09", "-75.91"],
               "New York": ["40.78", "-73.96"],
              "Chicago": ["41.98", "-87.9"],
              "Atlanta": ["33.66", "-84.42"],
              "Denver": ["39.87", "-104.67"]}
'''
label_lat = Label(root, text="Enter Latitude")
entry_lat = Entry(root, width=35, borderwidth=5, textvariable=lat)
label_lon = Label(root, text="Enter Longitude")
entry_lon = Entry(root, width=35, borderwidth=5, textvariable=lon)

forecast_button = Button(root, font = 24, text = "Get Forecast", 
                command=lambda: weekly_forecast(lat.get(), lon.get()))

close_button = Button(root, font = 24, text = "Close Window", 
                command=root.destroy)

dropdown = OptionMenu(root, city_select, *city_latlon)
choose_button = Button(root, text="Select", command=city_choice)
test_widget = Text(root, font = ("Helvitica", "16"),
                  height=10, width=25)

dropdown.pack(pady=20)
label_lat.pack()
entry_lat.pack()
label_lon.pack()
entry_lon.pack()
choose_button.pack(pady=10)
forecast_button.pack(pady=10)
test_widget.pack()
close_button.pack(pady=10)
'''


entry_frame = Frame(root)
entry_frame.grid(row=0, column=0)
drop_frame = Frame(root)
drop_frame.grid(row=0, column=1)

label_lat = Label(entry_frame , text="Enter Latitude").pack()
entry_lat = Entry(entry_frame , width=35, borderwidth=5, textvariable=lat).pack()
label_lon = Label(entry_frame , text="Enter Longitude").pack()
entry_lon = Entry(entry_frame , width=35, borderwidth=5, textvariable=lon).pack()
button = Button(entry_frame , font = 24, text = "Get Forecast", 
                command=lambda: weekly_forecast(lat.get(), lon.get()))
button.pack(pady = 20)

drop_label = Label(drop_frame, text="You can also select a city:").pack()
dropdown = OptionMenu(drop_frame, city_select, *city_list).pack()
choose_button = Button(drop_frame, text="Select City", command=city_choice)
choose_button.pack(pady = 20)

weather_text = Text(root, height=16)
weather_text.grid(columnspan=2)

button2 = Button(root, font = 24, text = "Close Window", 
                command=root.destroy)
button2.grid(columnspan=2, pady = 20)

root.mainloop()