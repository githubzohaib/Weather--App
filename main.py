from tkinter import *
import requests
from PIL import Image,ImageTk

root = Tk()

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1af504fb37eb81bc311babeb46c3e546").json()
    w_label_text.config(text=data["weather"][0]["main"])
    t_label_text.config(text=str(int(data["main"]["temp"]-273.15)))
    p_label_text.config(text=data["main"]["pressure"])
    h_label_text.config(text=data["main"]["humidity"])
    s_label_text.config(text=data["main"]["sea_level"])
    

root.title("Weather App")
root.geometry("2000x2000")

image= Image.open("Images/mountains.webp")
image= image.resize((1700,1500))
image_photo= ImageTk.PhotoImage(image)

img_label = Label(root,image=image_photo)
img_label.pack()

box_frame1 = Frame(img_label,bg="darkgreen")
box_frame1.place(x=240,y=100,width=1000,height=100)

city_name = StringVar()

text_box = Entry(box_frame1,font=("times new roman",45), textvariable=city_name)
text_box.place(x=10,y=10,width=720,height=80)

button_box = Button(box_frame1,text="Get Weather",font=("times new roman",25),fg="darkgreen",activeforeground="darkgreen",bd=5,
                    command=data_get)
button_box.place(x=790,y=10,width=200,height=80)

box_frame2= Frame(root,bg="darkgreen")
box_frame2.place(x=240,y=250,width=1000,height=450)

box_label = Label(box_frame2,font=40)
box_label.place(x=10,y=10,width=980,height=430)

# weather label-----------------------------------------
w_label = Label(box_label,text="Weather", font=("times new roman",40))
w_label.place(x=60,y=10,width = 500,height=70)

w_label_text= Label(box_label,font=("times new roman",30),bg="lightblue",fg="darkblue")
w_label_text.place(x=520,y=10,width=250,height=70)

# Temperature label ------------------------------------------
t_label = Label(box_label,text="Temperature", font=("times new roman",40))
t_label.place(x=60,y=90,width = 500,height=70)

t_label_text= Label(box_label,font=("times new roman",30),bg="lightblue",fg="darkblue")
t_label_text.place(x=520,y=90,width=250,height=70)

#Pressure--------------------------------------
p_label = Label(box_label,text="Pressure", font=("times new roman",40))
p_label.place(x=60,y=170,width = 500,height=70)

p_label_text= Label(box_label,font=("times new roman",30),bg="lightblue",fg="darkblue")
p_label_text.place(x=520,y=170,width=250,height=70)

#Humidity-----------------------------------------
h_label = Label(box_label,text="Humidity", font=("times new roman",40))
h_label.place(x=60,y=250,width = 500,height=70)

h_label_text= Label(box_label,font=("times new roman",30),bg="lightblue",fg="darkblue")
h_label_text.place(x=520,y=250,width=250,height=70)

# sea level----------------------------------------
s_label = Label(box_label,text="Sea Level", font=("times new roman",40))
s_label.place(x=60,y=330,width = 500,height=70)

s_label_text= Label(box_label,font=("times new roman",30),bg="lightblue",fg="darkblue")
s_label_text.place(x=520,y=330,width=250,height=70)


root.mainloop()