class Auction:
    auctioneers = []
    price = 1

    def addInAuction(self, auctioneer):
        self.auctioneers.append(auctioneer)

    def removeFromAuction(self, name):
        for auctioneer in self.auctioneers:
            if auctioneer.name == name:
                self.auctioneers.remove(auctioneer)
                break

    def isInAuction(self, name):
        for auctioneer in self.auctioneers:
            if auctioneer.name == name:
                return True
        return False

    def printAllAuctioneers(self):
        if len(self.auctioneers) == 0:
            print("No auctioneer available")
        else:
            for auctioneer in self.auctioneers:
                print("Auctioneer name: {}".format(auctioneer.name))

    def updatePrice(self, price, bidder):
        if price > self.price:
            self.price = price
            self.notifyAuctioneers(bidder)
        else:
            print("Amount must be greater than {}".format(self.price))

    def notifyAuctioneers(self, bidder):
        for auctioneer in self.auctioneers:
            auctioneer.update(self.price, bidder)

    def currentPrice(self):
        return self.price
