import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        self.is_on = True
        print("Thermometer is ON.")

    def turn_off(self):
        self.is_on = False
        print("Thermometer is OFF.")

    def measure_temperature(self):
        if not self.is_on:
            print("Cannot measure temperature. Thermometer is OFF.")
            return
        self.temperature = round(random.uniform(34.0, 42.0), 1)

    def display_temperature(self):
        if self.temperature is None:
            print("No temperature measured yet.")
            return

        message = f"Temperature: {self.temperature}C"
        if self.temperature >= 41.0:
            message += " (CRITICAL TEMPERATURE!!)"
        elif self.temperature >= 37.0:
            message += " (fever)"
        print(message)


thermo = Thermometer()
thermo.turn_on()
thermo.measure_temperature()
thermo.display_temperature()
thermo.turn_off()