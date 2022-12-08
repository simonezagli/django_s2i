from web3 import Web3


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/7c15c1346d4f44088e9583d5f4a05ac1'))
    address = '0x33e5663DEcCDc049953380d5102356423dcf179e'
    privateKey = '0x23d97115b6ff8df10bc81844f9d29426b7a91ad1f579af5f0e698c8b6ce4fcd5'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
