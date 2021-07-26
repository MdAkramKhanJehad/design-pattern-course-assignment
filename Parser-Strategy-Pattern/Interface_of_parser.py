from abc import ABC, abstractmethod


class InterfaceParser(ABC):
    @abstractmethod
    def convert(self, fileName):
        pass
