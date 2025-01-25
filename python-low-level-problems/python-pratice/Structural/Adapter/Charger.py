class USBDevice:
    def charge(self, power):
        print(f"Charging device with {power}")

class Socket:
    def provide_power(self):
        return "Standard AC Power"

class Adapter:
    def __init__(self, socket):
        self.socket = socket

    def get_usb_power(self):
        ac_power = self.socket.provide_power()
        return f"USB power derived from {ac_power}"
    

wall_socket = Socket()
usb_device = USBDevice()

adapter = Adapter(wall_socket)
usb_power = adapter.get_usb_power()
usb_device.charge(usb_power)