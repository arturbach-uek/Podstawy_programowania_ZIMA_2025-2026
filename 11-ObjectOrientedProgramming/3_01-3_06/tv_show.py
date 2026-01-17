from tv import TV

def main():
    my_tv = TV()
    print(my_tv.show_status())

    my_tv.toggle()
    print(my_tv.show_status())

    channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"]
    my_tv.set_channels(channels)
    my_tv.show_channels()
    print(my_tv.show_status())

    my_tv.set_channel(4)
    print(my_tv.show_status())

    for _ in range(5):
        my_tv.increase_volume()
        print(my_tv.show_status())

    for _ in range(3):
        my_tv.decrease_volume()
        print(my_tv.show_status())

    my_tv.toggle()
    print(my_tv.show_status())

if __name__ == "__main__":
    main()
