def time_string(hours, minutes, time_format):
    if time_format == "24":
        return f"{hours:02d}:{minutes:02d}"
    else:
        suffix = "am" if hours < 12 else "pm"
        display_hour = hours if 1 <= hours <= 12 else hours - 12 
        if display_hour == 0:
            display_hour = 12
        return f"{display_hour}:{minutes:02d}{suffix}"
        
print(time_string(15, 19, "12"))