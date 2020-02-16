
import time
import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash(data)


    def __repr__(self):
        return 'Block is: Timestamp :{} \n Data: {} \n Hash: {}'.format(self.timestamp,self.data, self.hash)

    @staticmethod
    def _calc_hash(string: str) -> str:
        """
        Calculates SHA-256 hash of an input string and return the hash.
        """
        sha = hashlib.sha256()
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()


class BlockChain(object):
    timestamp = time.ctime()
    def __init__(self):
        self.tail = None

    def append(self, data):
        """ Append a value to the end of the BlockChain. """

        timestamp = time.ctime()

        if self.tail is None:
            self.tail = Block(timestamp=timestamp, data=data, previous_hash=None)

        else:
            self.tail = Block(timestamp = timestamp, data=data, previous_hash=self.tail)


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
# Prints 0

print(blockchain.to_list())
# Prints []


blockchain.append('my balance: 0 | cash flow: +20 | final balance: 20')
print(blockchain.size())
# Prints 1

print(blockchain.to_list())

# Prints [['my balance: 0 | cash flow: +20 | final balance: 20', 'Wed Jan 29 20:03:02 2020', 'ad9f15fc3b3523462f04dd795b2af7ddc3a93f6e01c27dfd408502e3dfccb7a1']]

blockchain.append('my balance: 20 | cash flow: +75 | final balance: 95')
blockchain.append('my balance: 95 | cash flow: 100 | final balance: 195')
blockchain.append('my balance: 195 | cash flow: +5 | final balance: 200')

print(blockchain.size())
# Prints 4

print(blockchain.to_list())

# [['my balance: 195 | cash flow: +5 | final balance: 200', 'Wed Jan 29 20:03:02 2020', 'e998ddfad9e47bdd479a7bcb1f0cde0fc36ef3504251075ddf52182620ebfe19'], 
# ['my balance: 95 | cash flow: 100 | final balance: 195', 'Wed Jan 29 20:03:02 2020', '144a80b60726b3c10337abd123f3ac029f08f28bf2873a058a9259dd05fee69e'], 
# ['my balance: 20 | cash flow: +75 | final balance: 95', 'Wed Jan 29 20:03:02 2020', '4e05a2805065ee424e128d4434be6a3d296b12501427e202ea41b91a40873379'], 
# ['my balance: 0 | cash flow: +20 | final balance: 20', 'Wed Jan 29 20:03:02 2020', 'ad9f15fc3b3523462f04dd795b2af7ddc3a93f6e01c27dfd408502e3dfccb7a1']]

#  EDGE CASES
blockchain2 = BlockChain()
print(blockchain2.to_list())
# Prints []
print(blockchain2.append('| |'))
# Prints None

print(blockchain2.to_list())
# Prints [['| |', 'Wed Jan 29 20:06:15 2020', 'e23ca1cb4827355cdcad2a953b85d9b5a42ee2346b844bd69f5b5a6162dc2328']]

