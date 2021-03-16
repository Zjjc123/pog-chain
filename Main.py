from Blockchain import Blockchain
from Block import Block
import time
import json

blockchain = Blockchain()
blockchain.add_new_transaction("transaction 1")
blockchain.add_block(Block(1, "fake transaction", time.time(), "dcc0c1d14ebb81949ec55f2d5e34dac902295101bcc3d17d70c7a1fb7d35460b"), "0000e156e2174c758494d05d793a68a7fcf5e9611e416b4b5f40a71062aa83ba")
blockchain.mine()
blockchain.add_new_transaction("transaction 2")
blockchain.mine()
blockchain.add_new_transaction("POG CHAIN TO THE MOON!!!!")
blockchain.mine()

for block in blockchain.chain:
    print("--------------------")
    print("Block:         ", block.index)
    print("Transactions:  ", block.transactions)
    print("Timestamp:     ", block.timestamp)
    print("Hash:          ", block.hash)
    print("Previous Hash: ", block.previous_hash)

print("--------------------")