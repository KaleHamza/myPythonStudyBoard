Class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __Str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    def disconnected(self)
        self.connected = False
        print("Disconnected")  

Class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaning_pages = capacity
        
    def __str__(self)
        return f"{super().__str__()} ({self.remaining_pages})"
    
    def print(self, pages):
        if not self.connected:
            print("Not connected")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
         
