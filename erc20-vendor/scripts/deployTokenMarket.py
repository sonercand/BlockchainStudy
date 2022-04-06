from brownie import SafeTokenMarket, accounts, config
from web3 import Web3


safeTokenAddresKovan = "0xeC8551775BcB06E0A5092376b308b11c5566507c"  # "0x93FeA7aCC9A4AC2DA6eE3578fB876228A68A0100"


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    tst1 = SafeTokenMarket.deploy(
        safeTokenAddresKovan, {"from": account}, publish_source=True
    )


def main():
    deploy()
