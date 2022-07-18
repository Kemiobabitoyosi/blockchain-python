#!/usr/bin/python3
""" Block
"""
import time
from hashlib import sha256
import json

class Block:
    """
    """
    def __init__(self, new_index:int, transactions:list, timestamp:time.time, previous_hash:str, nonce=0):
        """
        """
        self.index = new_index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):

        # serializing 
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
