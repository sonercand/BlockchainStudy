from scripts.helpers import get_account
from scripts.get_weth import get_weth
from brownie import network, config, interface
from web3 import Web3

global AMOUNT
AMOUNT = Web3.toWei(0.1, "ether")


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
    # print(lending_pool)
    # approve sending out erc20 tokens
    approve_erc20(AMOUNT, lending_pool.address, erc20_address, account)


def get_lending_pool():
    # lending pool address can change time to time
    # documentation : https://docs.aave.com/developers/v/1.0/developing-on-aave/the-protocol/lendingpool
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    # ABI, address
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool


def approve_erc20(amount, spender, erc20_address, account):
    # ABI, address
    print("Approving erc20 token")
    erc20 = interface.IERC20(erc20_address)
    txn = erc20.approve(spender, amount, {"from": account})
    txn.wait(1)
    print("approved")
    return txn
