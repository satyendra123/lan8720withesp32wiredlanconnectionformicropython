import machine
import time

class Modbus:
    def __init__(self, uart_id=1, baudrate=9600, tx_pin=17, rx_pin=16):
        self.uart = machine.UART(uart_id, baudrate=baudrate, tx=tx_pin, rx=rx_pin)

    def send_receive(self, request):
        self.uart.write(request)
        time.sleep(0.1)  # Wait for the response
        response = self.uart.read()
        return response
