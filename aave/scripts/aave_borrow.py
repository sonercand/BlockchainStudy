from scripts.helpers import get_account
from scripts.get_weth import get_weth
from brownie import network, config, interface


def main():
    # get account
    account = get_account()
    # get weth token address
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    # exchange eth for weth if on mainnet fork
    if network.show_active() == "mainnet-fork-dev":
        get_weth()
    # borrow for aave using ABI and address
    lending_pool = get_lending_pool()


def get_lending_pool():
    # lending pool address can change time to time
    # documentation : https://docs.aave.com/developers/v/1.0/developing-on-aave/the-protocol/lendingpool
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool
    return None
