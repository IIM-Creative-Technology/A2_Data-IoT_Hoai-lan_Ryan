from machine import Pin,ADC
import utime
import ujson
import network
import urequests
import socket


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = 'Kirby'
password = 'cochonrouge'
wlan.connect(ssid, password)
url = "http://192.168.84.144:3000/"
print(wlan.isconnected())

# while not wlan.isconnected():
#     print("Waiting for co")
#     utime.sleep(1)
#     pass


# server connection
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        utime.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
    


# button

# Pin to which the button is connected
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)

while True:
    print(button_pin.value())
    try:
        print("Posting")
        r = urequests.post("http://192.168.84.144:3000/post" , headers={'Content-type': 'application/json'}, json={
            'button' : button_pin.value
        }) # lance une requete sur l'url
        # print(r.json()) # traite sa reponse en Json
        r.close() # ferme la demande
    except Exception as e:
        print(e)
    