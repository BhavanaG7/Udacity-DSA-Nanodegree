'''
--------------------------------------------------------------------------------------------------------------------------
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.


----------------------------------------------------------------------------------------------------------------------------
'''
import time
import hashlib


class Block:

    def __init__(self, data, prev_hash):
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self._calc_hash(data)

    def __repr__(self):
        return f'Blockchain : \n Timestamp: {self.timestamp}  \n Data: {self.data} \n Hash: {self.hash} \n Prev_Hash:{self.prev_hash}'

    @staticmethod
    def _calc_hash(string):
        sha = hashlib.sha256()
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def append(self, data):
        if self.tail is None:
            self.tail = Block(data=data, prev_hash=None)

        else:
            self.tail = Block(data=data, prev_hash=self.tail)

    def search(self, data):
        if self.tail is None:
            print("Add the data before searching it!")
            return

        else:
            head_pos = self.tail

            while head_pos.prev_hash:
                if head_pos.data == data:
                    return head_pos
                head_pos = head_pos.prev_hash

            return None

    #size of the blockchain
    def size(self):
        head_pos = self.tail
        length = 0

        while head_pos is not None:
            head_pos = head_pos.prev_hash
            length += 1

        return length

    #blockchain to list.
    def to_list(self):
        output_list = []
        val = self.tail
        while val:
            output_list.append([val.data, val.timestamp, val.hash])
            val = val.prev_hash
        return output_list

blockchain=BlockChain()

#size of blockchain
print(f"size : {blockchain.size()}")

print("-----------------------------------------------------------------")

#content of blockchain
print(f"content : \n {blockchain.to_list()}")

print("-----------------------------------------------------------------")

blockchain.append('initial: 0 | change value: +1 | final: 1')
print(f"size : {blockchain.size()}")
print(f"content : \n {blockchain.to_list()}")

print("-----------------------------------------------------------------")

blockchain.append('initial: 1 | change value: +19 | final: 20')
blockchain.append('initial: 20 | change value: +15 | final: 35')
blockchain.append('initial: 35 | change value: -5 | final: 30')
blockchain.append('initial: 30 | change value: +10 | final: 40')
print(f"size : {blockchain.size()}")
print(f"content : \n {blockchain.to_list()}")

print("-----------------------------------------------------------------")

#search
print(blockchain.search('initial: 20 | change value: +15 | final: 35'))

print("-----------------------------------------------------------------")

#edge case
print("When element is not found:")
print(blockchain.search('initial: 200 | change value: +150 | final: 350'))
print("-----------------------------------------------------------------")

blockchain = BlockChain()
#trying to add the value when size is 0
print(blockchain.search('initial: 20 | change value: +15 | final: 35'))