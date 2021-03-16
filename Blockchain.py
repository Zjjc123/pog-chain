import time
from Block import Block

class Blockchain:
    difficulty = 4

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    # create the first block in the blockchain
    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    # calculate a valid proof of work with a certain number of leading 0s
    def proof_of_work(self, block):
        # number of leading zeros
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            # adding 1 to the Nonce number changes the hash allowing a recomputation
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    # add a new block to the block chain
    def add_block(self, block, proof):
        previous_hash = self.last_block.hash
        # adding fails when the previous hash does not match with the previous hash of the block
        if previous_hash != block.previous_hash:
            return False
        # adding fails when the work is incorrect
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    # checks if the work is valid - if there are enough leading 0s
    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    # adding the transactions to unconfirmed - confirm once proof of work has been completed
    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    # mining
    def mine(self):
        # if the list is empty no need to mine
        if not self.unconfirmed_transactions:
            return False

        # store the last block in the chain
        last_block = self.last_block

        # create a new block storing the previous hash and the total transactions
        new_block = Block(index=last_block.index + 1,
                        transactions=self.unconfirmed_transactions,
                        timestamp=time.time(),
                        previous_hash=last_block.hash)

        # calculate a proof of work
        proof = self.proof_of_work(new_block)

        # add a block with the proofs
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index
