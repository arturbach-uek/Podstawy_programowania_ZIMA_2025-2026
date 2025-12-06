wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

with open('seven_wonders.txt', 'w') as file:
    [file.write(word + '\n') for word in sorted(wonders)]
