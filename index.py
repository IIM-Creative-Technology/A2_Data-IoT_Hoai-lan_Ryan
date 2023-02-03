from machine import Pin,ADC
import utime
import json
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
    sensorData = {'sensorData':yStatus}
    as_json = json.dumps(sensorData)
    print(sensorData)  # prints '<class 'dict'>'
    print(type(as_json))  # prints '<class 'str'>'
    as_object = json.loads(as_json)
    print(type(as_object))  # prints '<class 'dict'>'
    # response = urequests.post(url, json=sensorData)
    # faire comme avec stringify , tout dans un string
    utime.sleep(0.5)

"""
    if yValue>=30000 & yValue<=36000:
        yStatus = "middle"
    elif yValue <= 60000 & yValue >= 36000 :
        yStatus = "up"
    elif yValue >= 600:
        yStatus = "down"
    if joyStickValue == 0:
        joystickStatus = "pressed"
"""

"""
while(True):
    try:
        print("GET")
        r = urequests.get(url)
        print (r.json())
        r.close()
        utime.sleep(1)
    except Exception as e:
        print(e)
        """




"""
adc = ADC(Pin(26, mode=Pin.IN))
#pin +-
while True:
    val = adc.read_u16()
    val = val * (3.3 / 65535)
    print(round(val,2),"V")
    time.sleep_ms(100)
"""

"""exo3
pwm_led = PWM(Pin(15, mode= Pin.OUT))
pwm_led.freq(1_000)
while True:
    for i in range(65000):    
        pwm_led.duty_u16(i)
        utime.sleep(0.00001)
    for i in range(65000):    
        pwm_led.duty_u16(65000-i)
        utime.sleep(0.00001)

"""

#Exo2
#pin_button = Pin(18, mode=Pin.IN, pull = Pin.PULL_UP)

"""Exo1
pinNumber2 = 13
led2 = Pin(pinNumber2, mode=Pin.OUT)
pinNumber1 = 17
led1 = Pin(pinNumber1, mode=Pin.OUT)
pinNumber3 = 15
led3 = Pin(pinNumber3, mode=Pin.OUT)
"""

#while True:

    
"""    Exo2
    print(pin_button.value())
    utime.sleep(0.5)
"""
"""Exo1
    led1.toggle()
    utime.sleep(1)
    led2.toggle()
    utime.sleep(1)
    led3.toggle()
    utime.sleep(1)

"""


