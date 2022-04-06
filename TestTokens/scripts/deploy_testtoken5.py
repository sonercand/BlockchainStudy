from brownie import TestToken5, accounts, config
from web3 import Web3


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    tst1 = TestToken5.deploy(
        "test token 5", "tt5", {"from": account}, publish_source=True
    )


def main():
    deploy()
