class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def toggle(self):
        self.is_on = not self.is_on

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
    
    def set_channel(self, new_channel_no):
        if 1 <= new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
        else:
            print("Invalid channel number.")
    
    def set_channels(self, channels_list):
        self.channels = channels_list
        self.channel_no = 1 if channels_list else None

    def show_channels(self):
        if not self.channels:
            print("No channels available.")
            return

        print("Channel list:")
        for i, channel in enumerate(self.channels, start=1):
            print(f"{i}. {channel}")

    def show_status(self):
        if self.is_on:
            status = "TV is on"
            if self.channel_no and self.channels:
                status += f", channel {self.channel_no} ({self.channels[self.channel_no - 1]})"
            status += f", volume {self.volume}"
            return status
        else:
            return "TV is off"
    
