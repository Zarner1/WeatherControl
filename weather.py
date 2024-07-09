import customtkinter as ctk
import requests
from PIL import Image, ImageTk
from io import BytesIO


def weather_get():
    global text1

    textbig2 = ctk.CTkTextbox(window, 175, 200, corner_radius=5, bg_color="grey",border_color="yellow",border_width=3,font=("Helvetica",15))
    canvas.create_window(400, 600, window=textbig2)
    Api_Key = "30fe3b577ded8dc1441ad6359b821241"
    final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(text1.get(), Api_Key)
    result = requests.get(final_URL)
    data = result.json()

    if 'main' in data:
        temp1=data['main']['temp']-273.15
        temp1=round(temp1,2)
        datatext = f"Sıcaklık: {temp1} °C\nEnlem: {data['coord']['lat']}\nBoylam: {data['coord']['lon']}\nRüzgar Hızı: {data['wind']['speed']} m/s"

        textbig2.insert("1.0", datatext)
    else:

        textbig2.insert("1.0", "hava durumu verisi alinamadi")
    pass


window = ctk.CTk()
window.geometry("800x800")
window.config(bg="Grey")
window.title("Hava Durumu")
window.resizable(False, False)

img = requests.get("https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638886301/EducationHub/photos/lightning-bolts.jpg")
image_data = img.content
image = Image.open(BytesIO(image_data))
image = image.resize((800, 800))
tk_image = ImageTk.PhotoImage(image)



canvas = ctk.CTkCanvas(window, width=800, height=800, bg="Grey", )
canvas.pack(fill="both", expand=True)
canvas.create_image(400, 400, image=tk_image)
#istanbul
canvas.create_rectangle(50, 50, 175, 175, outline="blue", width=5)
canvas.create_text(110, 190, text="Istanbul", font=("Helvetica", 20), anchor="center", fill="red")
istanbulURL="http://api.openweathermap.org/data/2.5/weather?q=Istanbul&appid=30fe3b577ded8dc1441ad6359b821241"
response1=requests.get(istanbulURL)
dataIST=response1.json()
canvas.create_text(110,110,text=f"{round(dataIST['main']['temp']-273.15,2)} °C",font=("Helvetica",22),fill="Red")
#ankara
canvas.create_rectangle(350, 50, 475, 175, outline="blue", width=5)
canvas.create_text(410, 190, text="Ankara", font=("Helvetica", 20), anchor="center", fill="red")
ankaraURL="http://api.openweathermap.org/data/2.5/weather?q=Ankara&appid=30fe3b577ded8dc1441ad6359b821241"
response2=requests.get(ankaraURL)
dataANK=response2.json()
canvas.create_text(410,110,text=f"{round(dataANK['main']['temp']-273.15,2)} °C",font=("Helvetica",22),fill="Red")
#Izmır
canvas.create_rectangle(650, 50, 775, 175, outline="blue", width=5)
canvas.create_text(710, 190, text="Izmir", font=("Helvetica", 20), anchor="center", fill="red")
izmirURL="http://api.openweathermap.org/data/2.5/weather?q=Izmir&appid=30fe3b577ded8dc1441ad6359b821241"
response3=requests.get(izmirURL)
dataIZM=response3.json()
canvas.create_text(710,110,text=f"{round(dataIZM['main']['temp']-273.15,2)} °C",font=("Helvetica",22),fill="Red")
#şehir girme texti
canvas.create_text(400, 375, text="Şehiri Giriniz", font=("Helvetica", 18), anchor="center", fill="Orange")
text1 = ctk.CTkEntry(window, corner_radius=1, border_color="orange", border_width=3,
                     width=150, height=20)

canvas.create_window(400, 400, window=text1)
button1 = ctk.CTkButton(window, text="Click Me", font=("Helvetica", 14), corner_radius=1, border_color="grey",
                        border_width=3, command=weather_get)
canvas.create_window(400, 430, window=button1)

window.mainloop()

