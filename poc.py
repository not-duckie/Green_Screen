import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0

    timestamp = datetime.datetime.now()
    caseNo = 0
    account_id = 0
    

    def __init__(self, data,caseNo,account_id):
        self.data = data
        self.caseNo = caseNo
        self.account_id = account_id

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nTime: " + str(self.timestamp) + "\nBlock Data: " + str(self.data[:8]) + "\nHashes: " + str(self.nonce) + "\nAccount ID: " + str(self.account_id) + "\nCase Number: " + str(self.caseNo) + "\n--------------"

class Blockchain:

    diff = 0
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis",0,0)
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                #print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()
f = open('nice.zip','rb')
blockchain.mine(Block(f.read(),6547,25))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
