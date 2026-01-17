temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
pos_temp = list(filter(lambda city: temperatures[city] > 0, temperatures))
print("Cities with positive temperatures:", " ".join(pos_temp))