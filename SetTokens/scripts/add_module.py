from brownie import SetTokenCreator, config
from brownie import network, config, interface
from web3 import Web3

from brownie import network, config, accounts

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache_local"]

setTokenAddress = "0x125b515989698CD7d6103F790E3f1Fd823019bE4"


def get_account(index=None, id=None):
    """get account for testing"""
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def add_module():
    account = get_account()
    st = interface.ISetToken(setTokenAddress)
    st.mint("0x3427A6cC667798339C471EC3c75a10e4A642306c", 10, {"from": account})
    # st.addModule("0xd8EF3cACe8b4907117a45B0b125c68560532F94D", {"from": account})
    st.initializeModule({"from": account})
    print(1)


def main():
    add_module()
