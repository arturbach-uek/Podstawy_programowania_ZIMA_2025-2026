class Phone:
    def __init__(self, battery_level=100, is_on=False, storage_used=0):
        self.battery_level = battery_level
        self.is_on = is_on
        self.storage_used = storage_used

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Phone is now ON.")
        else:
            print("Phone is already ON.")

    def make_call(self, minutes):
        if self.is_on and self.battery_level > 0:
            print(f"Making a call for {minutes} minutes...")
            self.battery_level -= minutes * 1
            if self.battery_level < 0:
                self.battery_level = 0
            print(f"Call ended. Battery now at {self.battery_level}%.")
        else:
            print("Cannot make a call. Either phone is OFF or battery is dead.")

    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        print(f"Phone charged. Battery now at {self.battery_level}%.")

    def install_app(self, size):
        if self.is_on:
            self.storage_used += size
            print(f"Installed an app of {size} GB. Storage used: {self.storage_used} GB.")
        else:
            print("Cannot install app. Phone is OFF.")

my_phone = Phone(battery_level=50, is_on=False, storage_used=10)

print("Initial phone state:")
print("Battery:", my_phone.battery_level)
print("Is On:", my_phone.is_on)
print("Storage used:", my_phone.storage_used, "GB")
print()

my_phone.turn_on()
my_phone.make_call(20)
my_phone.install_app(2)
my_phone.charge(30)

print("\nFinal phone state:")
print("Battery:", my_phone.battery_level)
print("Is On:", my_phone.is_on)
print("Storage used:", my_phone.storage_used, "GB")
