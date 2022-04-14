from brownie import accounts, network, config
from brownie import SafeToken, Sales, KycContract
from web3 import Web3


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    st = SafeToken.deploy({"from": account}, publish_source=True)
    kyc = KycContract.deploy({"from": account}, publish_source=True)
    print(st.address)
    sales = Sales.deploy(
        1, account, st.address, kyc.address, {"from": account}, publish_source=True
    )


def main():
    deploy()
