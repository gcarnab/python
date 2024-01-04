""" 
Copyright (c) 2024 GCARNAB

"""
import sys

#sys.path.append("C:/DEV/workspace/vscode/python/GC_BLOCKCHAIN/Blockchain")

from .block import Block
from .blockheader import BlockHeader
from .database.database import BlockchainDB
from ..util.util import hash256

import time
import json

ZERO_HASH = '0' * 64
VERSION = 1
INITIAL_TARGET = 0x0000FFFF00000000000000000000000000000000000000000000000000000000
SAVE_ON_DISK = False

class Blockchain:

    def __init__(self):
        self.chain = []
        #self.GenesisBlock()

    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()
    
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"GC send {BlockHeight} BTC to K"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION,prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        print(
            f"Block {BlockHeight} mined successfully with Nonce value of {blockheader.nonce}"
        )  

        if SAVE_ON_DISK :
            #WRITE ON DISK     
            self.write_on_disk([Block(BlockHeight,1,blockheader.__dict__, 1, Transaction).__dict__])
        else :
            #WRITE ON CONSOLE
            self.chain.append(Block(BlockHeight,1,blockheader.__dict__, 1, Transaction).__dict__)
            print()
            print(json.dumps(self.chain, indent=4))

    def main(self):
        while True:
            lastBlock = self.fetch_last_block()
            if lastBlock is None:
                self.GenesisBlock()

            #WRITE ON CONSOLE
            #lastBlock = self.chain[::-1] 
            #BlockHeight = lastBlock[0]["Height"] + 1
            #print(f"Current Block Height is is {BlockHeight}")
            #prevBlockHash = lastBlock[0]["BlockHeader"]["blockHash"]

            #WRITE ON DISK
            lastBlock = self.fetch_last_block() #WRITE ON DISK
            BlockHeight = lastBlock["Height"] + 1
            prevBlockHash = lastBlock["BlockHeader"]["blockHash"]
            self.addBlock(BlockHeight, prevBlockHash)
