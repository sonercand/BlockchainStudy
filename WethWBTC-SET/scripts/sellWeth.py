from scripts.helpers import get_account
from brownie import config, network, interface


def main():
    sell_weth()


def sell_weth(val=1 * 10**18):
    """
    Get weth using ETH
    """
    # weth contract
    # get ABI , address
    account = get_account()
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    tx = weth.withdraw(val, {"from": account})
    print(f"Received 0.1 WETH")
    tx.wait(1)
    return tx
