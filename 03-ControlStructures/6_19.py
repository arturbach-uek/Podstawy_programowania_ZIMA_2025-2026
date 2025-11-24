print("SURVEY")

answer1 = input("Are you interested in computer science? (y/n): ").lower() == 'y'
answer2 = input("Do you like playing computer games? (y/n): ").lower() == 'y'
answer3 = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if answer1 else 'No'}")
print(f"Playing computer games: {'Yes' if answer2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if answer3 else 'No'}")
