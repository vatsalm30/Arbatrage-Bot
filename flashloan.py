import json
from web3 import Web3

web3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/d0cd9b8a582c43ac83e714006b792533'))
smart_contract_string = open('build\contracts\Flashloan.json', "r").read()
smart_contract_json = json.loads(smart_contract_string)

abi = smart_contract_json["abi"]
bytecode = smart_contract_json["bytecode"]
addr = '0x1e4D9a2EbbCD2cc36caF779Fb8f34ABEE3Af079b'
contract = web3.eth.contract(address=addr, abi=abi, bytecode=bytecode)
latestData = contract.functions.add(1, 2)
print(latestData)
