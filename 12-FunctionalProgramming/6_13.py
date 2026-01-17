import matplotlib.pyplot as plt

countries = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]

country_names = list(map(lambda c: c["country"], countries))
total_medals = list(map(lambda c: c["gold"] + c["silver"] + c["bronze"], countries))

plt.bar(country_names, total_medals, color='red')

plt.title("Total Medals Won by Each Country")
plt.xlabel("Country")
plt.ylabel("Total Medals")

# Display the chart
plt.show()
