from web3 import Web3

web3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/d0cd9b8a582c43ac83e714006b792533'))
abi = ''
addr = '0x1e4D9a2EbbCD2cc36caF779Fb8f34ABEE3Af079b'
contract = web3.eth.contract(address=addr, abi=abi)
latestData = contract.functions.latestRoundData().call()
print(latestData)
