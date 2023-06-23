import time
import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount, d_sig, sender_key):
        # sender's ID
        self.sender = sender
        # receiver's ID
        self.receiver = receiver
        # public key of sender
        self.sender_key = sender_key
        # amount sender send
        self.amount = amount
        # digital signature
        self.d_sig = d_sig






class Block:
    def __init__(self, transaction, previous_hash):
        self.timestamp = time.time()
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.transaction) + str(self.previous_hash)
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
