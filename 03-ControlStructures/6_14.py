facebook = True
twitter = False
instagram = True

accounts_count = 0
if facebook:
    accounts_count += 1
if twitter:
    accounts_count += 1
if instagram:
    accounts_count += 1

if accounts_count >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")
