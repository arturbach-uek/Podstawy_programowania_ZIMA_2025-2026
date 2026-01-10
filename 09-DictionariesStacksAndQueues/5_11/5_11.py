import json

try:
    with open('voting.json', 'r', encoding='utf-8') as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

person_name = input('Name of the person you are voting for: ')
votes[person_name] = votes.get(person_name, 0) + 1

with open('voting.json', 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent = 4)

print("Voting updated:", votes)
