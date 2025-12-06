with open('healthy_lifestyle.txt') as src, open('copy_healthy_lifestyle.txt', 'w') as dst:
    dst.write(src.read())
