
import time
import hashlib

class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash(data)

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)

    @staticmethod
    def _calc_hash(string: str) -> str:
        """
        Calculates SHA-256 hash of an input string and return the hash.
        """
        sha = hashlib.sha256()
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def append(self, data):
        """ Append a value to the end of the BlockChain. """

        if self.tail is None:
            self.tail = Block(data=data, previous_hash=None)

        else:
            self.tail = Block(data=data, previous_hash=self.tail)


    def size(self):
        """ Return the size or length of the BlockChain. """
        position_head = self.tail
        length = 0

        while position_head is not None:
            position_head = position_head.previous_hash
            length += 1

        return length

    def to_list(self):
        """Transforms the BlockChain content into a list"""
        out = []
        block = self.tail
        while block:
            out.append([block.data, block.timestamp, block.hash])
            block = block.previous_hash
        return out


# TEST CASE
blockchain = BlockChain()

print(blockchain.size())

print(blockchain.to_list())


blockchain.append('my balance: 0 | cash flow: +20 | final balance: 20')
print(blockchain.size())

print(blockchain.to_list())


blockchain.append('my balance: 20 | cash flow: +75 | final balance: 95')
blockchain.append('my balance: 95 | cash flow: 100 | final balance: 195')
# blockchain.append('my balance: 195 | cash flow: +5 | final balance: 200')

print(blockchain.size())

print(blockchain.to_list())


