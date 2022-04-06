from brownie import TestToken3, TestToken4, accounts, config
from web3 import Web3


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    tst1 = TestToken3.deploy(
        "test token 3", "tt3", {"from": account}, publish_source=True
    )
    tst2 = TestToken4.deploy(
        "test token 4", "tt4", {"from": account}, publish_source=True
    )


def main():
    deploy()
