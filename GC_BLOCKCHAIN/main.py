"""
GC BLOCKCHAIN SIMULATOR
Copyright (c) 2024 GCARNAB
"""

from Blockchain.Backend.core.blockchain import Blockchain
from multiprocessing import Process, Manager
from Blockchain.Frontend.run import main


if __name__ == "__main__":
    with Manager() as manager:
 
        #webapp = Process(target=main, args=())
        #webapp.start()

        blockchain = Blockchain()
        blockchain.main()