import time
from lan8720 import Lan8720
from modbus import Modbus
from soilmoisture import SoilMoistureSensor
from mqtt import MQTT

def main():
    while True:
        res = sm.get()
        if res is not None:
            print(res)
            mqtt.publish(sm.topic, res)
            time.sleep(20)
            continue
        time.sleep(10)

if __name__ == '__main__':
    lan = Lan8720()
    lan.active()
    time.sleep(2)
    print(lan.ifconfig())

    modbus = Modbus()
    sm = SoilMoistureSensor(modbus)
    mqtt = MQTT(
        '2000300436',
        '16687396.dev',
        debug=True,
    )
    mqtt.connect()
    main()
