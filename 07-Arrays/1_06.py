def weekday(n):
    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    
    return weekdays[n - 1]

print(weekday(int(input("Enter month number: "))))