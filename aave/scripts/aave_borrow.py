from scripts.helpers import get_account
from scripts.get_weth import get_weth
from brownie import network, config


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() == "mainnet-fork-dev":
        get_weth()
