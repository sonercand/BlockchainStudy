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
    tx = lending_pool.deposit(
        erc20_address, AMOUNT, account.address, 0, {"from": account}
    )
    tx.wait(1)
    print("depositing collateral")
    borrowable_eth, total_debth = get_borrowable_data(lending_pool, account)
    print("Borrowing assesment")
    dai_eth_price_feed = config["networks"][network.show_active()]["dai_eth_price"]
    dai_eth_price = get_asset_price(dai_eth_price_feed)
    print(f"dai_eth_price is {dai_eth_price}")
    amount_dai_to_borrow = (1 / dai_eth_price) * (
        float(Web3.toWei(borrowable_eth, "ether")) * 0.95
    )  # borow dai 95% of max
    print(f"amount to be borrowed: {amount_dai_to_borrow}")
    # get dai address
    dai_address = config["networks"][network.show_active()]["dai_token"]
    borrow_txn = lending_pool.borrow(
        dai_address,
        Web3.toWei(amount_dai_to_borrow, "ether"),
        1,
        0,
        account.address,
        {"from": account},
    )  # 1 is stable 2 is variable interest rate
    print("borrowing")
    borrow_txn.wait(1)
    get_borrowable_data(lending_pool, account)


def get_asset_price(price_feed_address):
    # abi address
    dai_eth_price_feed = interface.AggregatorV3Interface(price_feed_address)
    latest_price = dai_eth_price_feed.latestRoundData()[1]
    latest_price_in_eth = Web3.fromWei(latest_price, "ether")
    print(f"latest price dai/eth: {latest_price_in_eth}")
    return float(latest_price)


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


def get_borrowable_data(lending_pool, account):
    (
        total_collateral_eth,
        total_debth_eth,
        available_borrow_eth,
        current_liquidation_threshold,
        ltv,
        health_factor,
    ) = lending_pool.getUserAccountData(account.address)
    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debth_eth = Web3.fromWei(total_debth_eth, "ether")
    print(
        f"you have {total_collateral_eth} worth of ETH deposited \n You have borrowed already {total_debth_eth} eth \n you can borrow additionally {available_borrow_eth} eth."
    )
    return (float(available_borrow_eth), float(total_debth_eth))
