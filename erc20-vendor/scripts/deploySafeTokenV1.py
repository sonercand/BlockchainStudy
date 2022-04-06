from brownie import SafeTokenV2, accounts, config
from web3 import Web3

in_sup1 = Web3.toWei(1000, "ether")


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    tst1 = SafeTokenV2.deploy(in_sup1, {"from": account}, publish_source=True)


def main():
    deploy()
