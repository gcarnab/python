""" 
Copyright (c) 2024 GCARNAB
"""
import os
import json

"""
Class to write on disk
"""
class BaseDB:
    def __init__(self):
        self.basepath = "Blockchain/data"
        self.filepath = "/".join((self.basepath, self.filename))

    def read(self):
        if not os.path.exists(self.filepath):
            print(f"File {self.filepath} not available")
            return False

        with open(self.filepath, "r") as file:
            raw = file.readline()

        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

    def write(self, item):
        data = self.read()
        if data:
            data = data + item
        else:
            data = item
        
        with open(self.filepath, "w+") as file:
            file.write(json.dumps(data))


class BlockchainDB(BaseDB):
    def __init__(self):
        self.filename = "gc_blockchain"
        super().__init__()

    def lastBlock(self):
        data = self.read()

        if data:
            return data[-1]


class AccountDB(BaseDB):
    def __init__(self):
        self.filename = "account"
        super().__init__()