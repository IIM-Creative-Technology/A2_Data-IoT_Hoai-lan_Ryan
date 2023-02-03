from machine import Pin,ADC
import utime
import ujson
import network
import urequests
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = 'Kirby'
password = 'cochonrouge'
wlan.connect(ssid, password)
url = "http://192.168.202.144:3000/"
print(wlan.isconnected())

while not wlan.isconnected():
    print("Waiting for co")
    utime.sleep(1)
    pass

yAxis = ADC(Pin(27))
joystick= Pin(16,Pin.IN, Pin.PULL_UP)

# à utiliser si la connextion ne marche pas
# data = {"value1": 42, "value2": "hello world"}
# headers = {'Content-Type': 'application/json'}
# response = urequests.post(url, json=data, headers=headers)
# if response.status_code == 200:
#     print("Data sent successfully")
# else:
#     print("Failed to send data")

# Pin to which the button is connected
button_pin = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)

# Function to send a request to the Node.js server
def send_request():
    print("send")
    
    """response = urequests.get(url)
    print(response.json())
    if response.status_code == 200:
        print("Button click event sent successfully")
    else:
        print("Failed to send button click event")
    response.close()"""
    try:
        print("GET")
        r = urequests.get("http://192.168.202.144:3000/") # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)
    
# Add an interrupt handler for the button pin

#button_pin.irq(trigger=Pin.IRQ_RISING, handler=send_request)

while True:
    print(button_pin.value())
    time.sleep(0.5)
    #button_pin.irq(trigger=Pin.IRQ_RISING, handler=send_request)
    #if(button_pin.value() == 0):
    send_request()


# while True:
#     yValue = yAxis.read_u16()
#     joyStickValue= joystick.value()
#     yStatus = "middle"
#     joystickStatus = "Not pressed"
#     if yValue>=5000 and yValue<=30000:
#         yStatus = "middle"
#     elif yValue <= 80000 and yValue >= 30000 :
#         yStatus = "up"
#     elif yValue >= 600 and yValue <= 5000:
#         yStatus = "down"
#     if joyStickValue == 0:
#         joystickStatus = "pressed"
#     print("X: " + yStatus + " -- Joystic " + joystickStatus)
#     print(str(yValue) +" -- " + str(joyStickValue))
#     sensorData = {'sensorData':yStatus}
#     as_json = json.dumps(sensorData)
#     print(sensorData)  # prints '<class 'dict'>'
#     print(type(as_json))  # prints '<class 'str'>'
#     as_object = json.loads(as_json)
#     print(type(as_object))  # prints '<class 'dict'>'
#     # response = urequests.post(url, json=sensorData)
#     # faire comme avec stringify , tout dans un string
#     utime.sleep(0.5)