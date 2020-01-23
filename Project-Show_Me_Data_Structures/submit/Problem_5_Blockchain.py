
import time
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Calculates SHA-256 hash of an input string and return the hash.
        """
        sha = hashlib.sha256()

        hash_string = str(self.data).encode('utf-8')

        sha.update(hash_string)

        return sha.hexdigest()

    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))

class Blockchain:

    def __init__(self):
        self.current_block = None

    def update_block (self, value):
        timestamp = time.gmtime()
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(timestamp, data, previous_hash)

blockchain = Blockchain()

blockchain.update_block (10)
print(blockchain.current_block)

blockchain.update_block (20)
print(blockchain.current_block)

blockchain.update_block (30)
print(blockchain.current_block)