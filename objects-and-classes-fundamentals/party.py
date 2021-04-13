class Party:
    def __init__(self):
        self.people = []


party = Party()

guests = input()

while not guests == "End":
    party.people.append(guests)
    guests = input()

print(f"Going: {', '.join(party.people)}" )
print(f"Total: {len(party.people)}")
