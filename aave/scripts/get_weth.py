from scripts.helpers import get_account
from brownie import config, network, interface


def main():
    get_weth()


def get_weth():
    """
    Get weth using ETH
    """
    # weth contract
    # get ABI , address
    account = get_account()
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    print(f"Received 0.1 WETH")
    tx.wait(1)
    return tx
