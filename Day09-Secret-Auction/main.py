from art import logo

print(logo)

users = {}
other_bidders = True
winner = ""
largest = 0

while other_bidders:
    user = input("What is your name?: ")
    bid = int(input("What is your bid: $"))

    users[user] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'\n ").lower() == "no":
        other_bidders = False

    print("\n" * 20)   #clean output window

    for key in users:        # finds winner
        val = users[key]
        if val > largest:
            winner = key

print(f"The winner is {winner} with a bid of ${users[winner]}")