from art import logo as picture
print(picture)

def find_the_highest_bidder(bids):
    winner = ''
    biggest_amount = 0
    for name in bids:
        highest_amount1 = bids[name]
        if highest_amount1 > biggest_amount:
            biggest_amount = highest_amount1
            winner = name
    print(f"The winner is {winner} with a bid of ${biggest_amount}.")


dictionary_buyers = {}
auction_continue = True
while auction_continue:
    # Ask for bidder's name and bid
    a_name = input("What is your name? ")
    a_bid = int(input("What's your bid? $"))  # Convert bid to integer for comparison
    dictionary_buyers[a_name] = a_bid

    # Ask if there are other bidders
    asking_for_other_buyers = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    # If no other bidders, end the auction
    if asking_for_other_buyers == "no":
        auction_continue = False
        find_the_highest_bidder(dictionary_buyers)
    elif asking_for_other_buyers == 'yes':
        print("\n" * 20)


# Find the highest bidder
# highest_bidder = max(dictionary_buyers, key=dictionary_buyers.get)
# highest_bid = dictionary_buyers[highest_bidder]

