import matplotlib.pyplot as plt

temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

cities = list(map(str, temperatures.keys()))
temps = list(map(int, temperatures.values()))

plt.bar(cities, temps, color='red')

plt.title("Temperatures Recorded in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

plt.show()
