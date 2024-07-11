class SoilMoistureSensor:
    def __init__(self, modbus, topic="soilmoisture/sensor"):
        self.modbus = modbus
        self.topic = topic

    def get(self):
        # Send Modbus request to read soil moisture sensor data
        request = b'\x04\x03\x00\x00\x00\x02'
        response = self.modbus.send_receive(request)
        if response:
            # Process the response here (e.g., extract the soil moisture value)
            # Assuming the response format is: 04 03 08 01 ...
            return response[3:7]
        else:
            return None
