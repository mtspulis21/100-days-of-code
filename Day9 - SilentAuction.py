bids = {}
stopped = False

def finding_highest(register):
    highest_bid = 0
    winner = ""
    # dict model {"Matheus":123,"John":124}
    for bidder in register:
        bid_amount = register[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    ordered_bids = sorted(bids.items(), key=lambda x:x[1],reverse=True)
    print(f"Winner: {winner} - Amount: {highest_bid}")
    print(f"Bids ranking: {ordered_bids}")

while not stopped:
    name = input("Please enter your name: ")
    bid = float(input("Please enter your bid value: "))
    bids[name] = bid
    end_bidding = input("Do you want to enter another bid? Y or N?").lower()
    if end_bidding == "n":
        stopped = True
        finding_highest(bids)