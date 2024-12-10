import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()



class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, last_block.hash)
        self.chain.append(new_block)


my_blockchain = Blockchain()

my_blockchain.add_block("Pransh sent 5 BTC to Alex")
my_blockchain.add_block("Alex sent 2 BTC to Casey")
my_blockchain.add_block("Casey sent 1 BTC to Jamie")


for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}\n")
