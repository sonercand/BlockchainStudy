from brownie import TestToken1, TestToken2, accounts, config
from web3 import Web3

in_sup1 = Web3.toWei(1000, "ether")
in_sup2 = Web3.toWei(1000, "ether")


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    tst1 = TestToken1.deploy(in_sup1, {"from": account}, publish_source=True)
    tst1.wait(1)
    tst2 = TestToken2.deploy(in_sup2, {"from": account}, publish_source=True)


def main():
    deploy()
