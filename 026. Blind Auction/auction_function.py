def add_bid(name_bid,price,bid_l):
    bid_l[name_bid] = price
    return bid_l

def check_bid_winner(bid_l):
    winner = ["name",0]
    for item in bid_l:
        if winner[1] < bid_l[item]:
            winner[0] = item
            winner[1] = bid_l[item]
    return winner

def print_bids(bid_l):
    print("The participants taking part in the auction:")
    for index,item in enumerate(bid_l):
        print(f"{index+1}. {item} : ${bid_l[item]}")

logo = """
██████╗ ██╗     ██╗███╗   ██╗██████╗      █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║     ██║████╗  ██║██╔══██╗    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝██║     ██║██╔██╗ ██║██║  ██║    ███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══██╗██║     ██║██║╚██╗██║██║  ██║    ██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
██████╔╝███████╗██║██║ ╚████║██████╔╝    ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                 
"""