from web3.middleware import geth_poa_middleware
# import json
from web3 import Web3
import solcx

solcx.install_solc()

source = "contracts/Counter.sol"
file = "Counter.sol"
spec = {
    "language": "Solidity",
    "sources": {
        file: {
                "urls": [
                    source
                ]
        }
    },
    "settings": {
        "optimizer": {
            "enabled": True
        },
        "outputSelection": {
            "*": {
                "*": [
                    "metadata", "evm.bytecode", "abi"
                ]
            }
        }
    }
}
out = solcx.compile_standard(spec, allow_paths=".")

ganache_url = "HTTP://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

abi = out['contracts']['Counter.sol']['Counter']['abi']
bytecode = out['contracts']['Counter.sol']['Counter']['evm']['bytecode']['object']

me = w3.eth.get_accounts()[0]
temp = w3.eth.contract(bytecode=bytecode, abi=abi)
txn = temp.constructor().buildTransaction({"from": me})
txn_hash = w3.eth.send_transaction(txn)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
address = txn_receipt['contractAddress']

counter = w3.eth.contract(address=address, abi=abi)
counter.functions.read().call()
txn_hash = counter.functions.increment().transact({"from": me})
w3.eth.wait_for_transaction_receipt(txn_hash)
counter.functions.read().call()
