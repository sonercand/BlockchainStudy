from brownie import SetTokenCreator, config
from brownie import network, config, interface
from web3 import Web3

from brownie import network, config, accounts

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


def deploy_token_set():
    account = get_account()

    stc = interface.ISetTokenCreator(
        config["networks"][network.show_active()]["contracts"]["SetTokenCreator"]
    )
    print(stc.address)
    add = stc.create(
        [
            "0x04d0DD2E72615DD3f88C5622c6Acf67E6009b859",
            "0x9eD89272C846DC7BEacE48f8003E44C6Ab0855FC",
        ],
        [10, 29],
        [
            "0x8a070235a4B9b477655Bf4Eb65a1dB81051B3cC1",
            "0xE038E59DEEC8657d105B6a3Fb5040b3a6189Dd51",
            "0x6BD69bf1FE2B1464a3017Da50fe4ca7c1779F8f6",
        ],
        "0x3427A6cC667798339C471EC3c75a10e4A642306c",
        "test_etf",
        "tef",
        {"from": account},
    )
    # setToken = interface.ISetToken("0x90Cc51D4eD75C13DcDe137627E2De3Ead727b831")
    # setToken.addModule("0x8a070235a4B9b477655Bf4Eb65a1dB81051B3cC1", {"from": account})
    # setToken.initialize()


def main():
    deploy_token_set()
