from Auction import Auction
from Auctioneer import Auctioneer


def selectOptions(auction):
    while True:
        print("\nWhat is do you want?\n1) Join Auction \t2) Bid \t3) Leave the auction \t4) See current auctioneers "
              "\t5) Exit")
        print("***** Current Price: {} *****".format(auction.currentPrice()))

        x = int(input())
        if x == 1:
            print("Enter name:", end=' ')
            name = input()
            auctioneer = Auctioneer(name)
            auction.addInAuction(auctioneer)

        elif x == 2:
            print("Enter bidder name: ", end='')
            name = input()
            if auction.isInAuction(name):
                print("Enter amount: ", end='')
                amount = float(input())
                auction.updatePrice(amount, name)
            else:
                print("Wrong Name. Try again")

        elif x == 3:
            print("Enter name: ", end='')
            name = input()
            if auction.isInAuction(name):
                auction.removeFromAuction(name)

        elif x == 4:
            auction.printAllAuctioneers()

        else:
            break


def main():
    auction = Auction()
    selectOptions(auction)


if __name__ == "__main__":
    main()
