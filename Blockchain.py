#SimpleBlockchain With Python
import hashlib
from crypto_minr import Miner

Limit=1000000000

Transaction=False
class RandomCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list,):
        self.previous_block_hash=previous_block_hash
        self.transaction_list=transaction_list

        self.block_data="-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()


Block=[]
Chain=[]

def hash(T):
    initial_block=RandomCoinBlock("initial String",[T])
    print(initial_block.block_data)
    print(initial_block.block_hash)
    Block.append(initial_block.block_hash )
    Miner(Block)
    chain_data=open("Blockcahin.csv","a")
    chain_data.write(str(Block))
    chain_data.close()
    Transaction=True
    if Transaction:
        Chain.append(Block)
        print(Chain)
        

    Block.clear

def wallet(User_id,Amount):
    ACCOUNT_BLANCE=0
    if Amount >0:
        ACCOUNT_BLANCE=+Amount
        Limit=-Amount
    if Limit == 0:
        print("Systam out of Rcb")


    print(ACCOUNT_BLANCE)

