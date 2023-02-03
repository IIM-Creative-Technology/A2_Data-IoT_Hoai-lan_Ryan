from machine import Pin,ADC
import utime
import ujson
import network
import urequests

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = 'RyanBgCosmique'
password = '1234567890'
wlan.connect(ssid, password)
url = "http://192.168.202.147:4000/"
print(wlan.isconnected())

"""while not wlan.isconnected():
    print("Waiting for co")
    utime.sleep(1)
    pass
"""
yAxis = ADC(Pin(27))
joystick= Pin(16,Pin.IN, Pin.PULL_UP)

# data = {"value1": 42, "value2": "hello world"}
# headers = {'Content-Type': 'application/json'}
# response = urequests.post(url, json=data, headers=headers)
# if response.status_code == 200:
#     print("Data sent successfully")
# else:
#     print("Failed to send data")

# Pin to which the button is connected
button_pin = machine.Pin(14, machine.Pin.IN, pin.PULL_DOWN)

# Function to send a request to the Node.js server
def send_request():
    response = urequests.get("http://your-nodejs-server.com/api/button-click")
    if response.status_code == 200:
        print("Button click event sent successfully")
    else:
        print("Failed to send button click event")

# Add an interrupt handler for the button pin
button_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=send_request)



"""
while True:
    yValue = yAxis.read_u16()
    joyStickValue= joystick.value()
    yStatus = "middle"
    joystickStatus = "Not pressed"
    if yValue>=5000 and yValue<=30000:
        yStatus = "middle"
    elif yValue <= 80000 and yValue >= 30000 :
        yStatus = "up"
    elif yValue >= 600 and yValue <= 5000:
        yStatus = "down"
    if joyStickValue == 0:
        joystickStatus = "pressed"
    print("X: " + yStatus + " -- Joystic " + joystickStatus)
    print(str(yValue) +" -- " + str(joyStickValue))
    # data = {"data":yStatus}
    # response = urequests.post(url, json=data)
    utime.sleep(0.1)
"""
