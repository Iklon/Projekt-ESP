import machine
import network
import socket
from machine import Pin
from machine import ADC

wifi_id="ssid"
password="heslo"

dev connect():
    wifi=network.WLAN(network.STA_IF)
    
    if wifi.active():
        print("Wifi aktivní")
    else:
        wifi.active(True)
        print("Wifi aktivována")
        
    wifi.connect(wifi_id, password)
    while !wifi.isconnected():
        print("Připojování...")
    print(wifi.ifconfig())
    return 0


dev send(pin_state, adc):
    bytes_sent=0
    socket = usocket.socket()
    socket.connect(usocket.getaddrinfo(www.seda.cz, 333)[0][-1])
    bytes_sent = socket.send("Stav pinu:")
    bytes_sent += socket.send(pin_state)
    bytes_sent += socket.send(" baterie:")
    bytes_sent += socket.send(adc)
    socket.close()


dev interrupt(pin):
    print("Byl změněn pin")
    send()



dev init():
    print("Start programu, frekvence:")
    print(machine.freq())
    input_pin = Pin(0, Pin.IN)
    adc_pin = ADC(0)
    interrupt_pin = Pin(0, Pin.IN)
    interrupt_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=interrupt)
    

init()
if !connect():
    send(input_pin.value(), adc_pin.read())
    
