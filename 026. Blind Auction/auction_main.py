from auction_function import print_bids,add_bid,check_bid_winner,logo

bid_list = dict()
while True:
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid amount? $"))
    add_bid(name,bid,bid_list)
    other_bid = input("Are there any other bidder?(Y/N) ").upper()
    print("\033[2J")
    if other_bid == "N":
        break

auction_winner = check_bid_winner(bid_list)
print(logo)
print_bids(bid_list)
print(f"The winner is {auction_winner[0]} with a bid of ${auction_winner[1]}")
