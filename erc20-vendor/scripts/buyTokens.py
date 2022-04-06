from web3 import Web3

from brownie import config, network, interface, accounts


def main():
    buyTokens()


def buyTokens():
    """
    Get weth using ETH
    """
    # weth contract
    # get ABI , address
    account = accounts.add(config["wallets"]["from_key"])
    stm = interface.ISafeTokenMarket("0xe563944F69fA6a23FF243Ee8227E94182c9Bf8aa")
    print(stm.address)
    tx = stm.buyTokens({"from": account, "value": 0.3 * 10**18})
    tx.wait(1)
    return tx
