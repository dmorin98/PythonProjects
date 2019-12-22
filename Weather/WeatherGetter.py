import tkinter as tk
import requests
from tkinter import font

height = 400
width = 800

font_fam = 'Fixedsys'
font_size = 15

color1='#DAF7A6'
color2='#FF5733'
color3='#FFC300'
#

def curr_format(weather):
    try:
        name = weather['city']['name']
        desc = weather['list'][0]['weather'][0]['description']
        temp = weather['list'][0]['main']['temp']
        feels_like = weather['list'][0]['main']['feels_like']

        final_str = 'Current Conditions\n\nCity %s \nConditions: %s  \nTemperature(C):%s C\nFeels Like:%s C' % (name,desc,temp,feels_like)

    except Exception as e:
        print(e)
        final_str ='Invalid City'

    return final_str

def next_format(weather):
    try:
        name = weather['city']['name']
        desc = weather['list'][1]['weather'][0]['description']
        temp = weather['list'][1]['main']['temp']
        feels_like = weather['list'][1]['main']['feels_like']

        final_str = 'Tomorrows Conditions\n\nCity %s \nConditions: %s  \nTemperature:%s C\nFeels Like:%s C' % (name,desc,temp,feels_like)

    except Exception as e:
        print(e)
        final_str ='Invalid City'

    return final_str

def weather(city):
    key = 'b8f34525e5f57aaf94e587db6f43e902'
    url = 'https://api.openweathermap.org/data/2.5/forecast?id={city ID}'
    params = {'APPID' : key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    #print(response.json())
    #Replacing Data for Left Side (Current Weather)
    label_left['text'] = curr_format(weather)
    label_right['text'] = next_format(weather)
    


root = tk.Tk() #Root Window

canvas = tk.Canvas(root, height = height, width = width)
canvas.pack()

background_imag = tk.PhotoImage(file='clouds.png')
background_label = tk.Label(root, image=background_imag)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg=color1, bd=5)
frame.place(relx=0.5, rely=0.10, relwidth=0.75, relheight=0.1, anchor='n')

entry =tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Fetch Weather", font = (font_fam, font_size),activebackground = color1,bd = 5, command=lambda: weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg=color2, bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#Current Weather Label(LEFT)
label_left = tk.Label(lower_frame, text = 'Current Weather', bg=color3, font = (font_fam, font_size))
label_left.pack(side='left')

#Tomorrows Weather Data(RIGHT)
label_right = tk.Label(lower_frame, text = 'Tomorrows Weather', bg=color3, font = (font_fam, font_size))
label_right.pack(side='right')



root.mainloop()