class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name}  via   {self.connected_by}   status {self.connected}"

    def disconnect(self):
        self.connected = False
        print("Device Disconnected Successfully")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remainimng_pages = capacity

    def __str__(self):
        return f"{super().__str__()} \nPages can be Printed upto :- {self.remainimng_pages} Capacity = {self.capacity}"

    def print(self,pages):
        if self.connected == True:
            print(f"Printing {pages} pages.")
            self.remainimng_pages -= pages
        else:
            print("Ypur Printer is not Connected")

p = Printer("printer","Bluetooth",500)
p.print(20)
print(p)
p.disconnect()
p.print(500)
print(p)