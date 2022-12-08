from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/7c15c1346d4f44088e9583d5f4a05ac1'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex ()
address = account.address
print(f"Your address: (address) \nYour key: (privateKey)")