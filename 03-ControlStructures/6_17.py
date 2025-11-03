time_24 = input("Enter time (24-hour format hh:mm): ")

hours, minutes = map(int, time_24.split(":"))

if hours == 0:
    hours_12 = 12
    period = "am"
elif 1 <= hours < 12:
    hours_12 = hours
    period = "am"
elif hours == 12:
    hours_12 = 12
    period = "pm"
else:  
    hours_12 = hours - 12
    period = "pm"

print(f"Time in 12-hour format: {hours_12}:{minutes:02d}{period}")
