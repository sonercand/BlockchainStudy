from typing import Set
from brownie import interface
from scripts.helpers import get_account

setTokenAddress = "0xdA3e2A919b0CB5Fcd7D91e2524f0D57d531eaAb9"
componenet = "0xd0A1E359811322d97991E03f863a0C30C2cF029C"
amount = 100
symbol = "TWS"


def run():
    account = get_account()
    basicIssuanceAddress = "0x8a070235a4B9b477655Bf4Eb65a1dB81051B3cC1"
    initialHook = "0x0000000000000000000000000000000000000000"
    setToken = interface.ISetToken(setTokenAddress)
    issuance = interface.IBasicIssuanceModule(basicIssuanceAddress)
    # issuance.initialize(setTokenAddress, initialHook, {"from": account})
    # need to approve issuance address on weth address
    print("init issuance")
    issuance.issue(
        setTokenAddress,
        100 * 10**18,
        account,
        {"from": account},
    )


def main():
    run()
