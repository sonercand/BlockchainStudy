from brownie import interface
from scripts.helpers import get_account


def run():
    account = get_account()
    usdcSetAddress = "0x7dE29E9761cF7052d076277A759D6b50EAb25842"
    basicIssuanceAddress = "0x8a070235a4B9b477655Bf4Eb65a1dB81051B3cC1"
    initialHook = "0x0000000000000000000000000000000000000000"
    setToken = interface.ISetToken(usdcSetAddress)
    issuance = interface.IBasicIssuanceModule(basicIssuanceAddress)
    print("initialised settoken and issuance")
    # issuance.initialize(usdcSetAddress, initialHook, {"from": account})
    print("initialised")
    # res = issuance.getRequiredComponentUnitsForIssue(
    #    usdcSetAddress, 100, {"from": account}
    # )
    # print(res)
    # setToken.editDefaultPositionUnit(usdcSetAddress, 0, {"from": account})
    # print("position set to default")
    setToken.mint(account, 1 * 10**18, {"from": account})
    print("minted")
    issuance.issue(usdcSetAddress, 10 * 10**18, account, {"from": account})


def main():
    run()
