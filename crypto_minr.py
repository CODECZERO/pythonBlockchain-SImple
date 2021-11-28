import hashlib
import Blockchain
miner=False
Rcb_limit=10000000000
zeroes=4
def Miner(Block):
    for Rcb in range(Rcb_limit):
        base_text=str(Block) +  str(Rcb)
        hash_try=hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f'"Found hash with rcb":{Rcb}')
            return hash_try
            

