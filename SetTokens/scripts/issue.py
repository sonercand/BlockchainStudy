from brownie import network, config, interface, accounts
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache_local"]


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


account = get_account()
setTokenAd = "0xce759369aE9e5E4D2837753a01dA1d0e848DF075"


def issue():
    ism = interface.IIssuerModule("0x8a070235a4B9b477655Bf4Eb65a1dB81051B3cC1")
    print(ism.address)
    ism.issue(
        setTokenAd, 1, "0x3427A6cC667798339C471EC3c75a10e4A642306c", {"from": account}
    )


def main():
    issue()
