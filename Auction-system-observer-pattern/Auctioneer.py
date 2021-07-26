from abc import ABC, abstractmethod


class AuctioneerInterface(ABC):
    @abstractmethod
    def update(self, price, bidder):
        pass


class Auctioneer(AuctioneerInterface):
    def __init__(self, name):
        self.name = name

    def update(self, price, bidder):
        print("Name: {} || Current print: {} || Bid by: {}".format(self.name, price, bidder))
