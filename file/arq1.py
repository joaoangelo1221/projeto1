from tkinter import *
import phonenumbers

import certifi
import ssl

from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from PIL import Image, ImageTk
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz



root=Tk()
root.title("Rastreador")
root.geometry("365x584")
root.resizable(False,False)

def tracker():
    enter_numero=entry.get()
    number=phonenumbers.parse(enter_numero)
    local=geocoder.description_for_number(number, 'en')
    cidade.config(text=local)

    operadora=carrier.name_for_number(number, 'en')
    cidade.config(text=operadora)

    horario=timezone.time_zones_for_number(number)
    cidade.config(text=horario)

    geolocal=Nominatim(user_agent="geopiExercises")
    localizacao=geolocal.geocode(local)

    lng=localizacao.longitude
    lat=localizacao.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=localizacao.longitude,lat=localizacao)
    home=pytz.timezone(result)
    local_time = datetime.now(home)
    current_time=current_time.strftime("%I:%M:%p")
    clock.config(text=current_time)



# carregar a logo do sistema
logo=PhotoImage(file="logo.png")
Label(root,image=logo).place(x=300, y=70)

# colocando icon no formulario
icon = Image.open('logo.png')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)

#label do cabeçalho
Cabecalho = Label(root,text="Rastreamento de Tefelone", font=("arial", 15, "bold"),justify="center")
Cabecalho.place(x=25,y=70)
#caixa de texto do cabeçalho
entry_Cabecalho = PhotoImage(file="pesquisa.png")
Label(root,image=entry_Cabecalho).place(x=55,y=100)
#caixa de texto do cabeçalho
entry=StringVar()
enter_numero =Entry(root, textvariable=entry,width=20,bd=5,font=("arial",10))
enter_numero.place(x=95,y=215)
#botao ok de pesquisa
Pesquisar_image = PhotoImage(file="ok.png")
Pesquisar= Button(image=Pesquisar_image,borderwidth=0,cursor="hand2",bd=2, font=("arial",10),command=tracker)
Pesquisar.place(x=165,y=260)

Box_pesquisar = PhotoImage(file="painel.png")
Label(root,image=Box_pesquisar).place(x=55,y=320)

cidade = Label(root,text="Cidade: ",fg="black",font=("arial", 7, "bold"))
cidade.place(x=100,y=400)

operadora = Label(root,text="Operadora: ",fg="black",font=("arial", 7, "bold"))
operadora.place(x=100,y=418)

zona = Label(root,text="País: ",fg="black",font=("arial", 7, "bold"))
zona.place(x=100,y=438)

horario = Label(root,text="Horário: ",fg="black",font=("arial", 7, "bold"))
horario.place(x=100,y=458)

longitude = Label(root,text="Longitude: ",fg="black",font=("arial", 7, "bold"))
longitude.place(x=100,y=478)

latitude = Label(root,text="Latitude: ",fg="black",font=("arial", 7, "bold"))
latitude.place(x=100,y=498)

ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL

root.mainloop()