from scripts.helpers import get_account
from brownie import config, network, interface

usdcAddress = "0xe22da380ee6B445bb8273C81944ADEB6E8450422"

initialWethAmount = 1
BasicIssuanceModule = "0x8a070235a4B9b477655Bf4Eb65a1dB81051B3cC1"
StreamingFeeModule = "0xE038E59DEEC8657d105B6a3Fb5040b3a6189Dd51"
TradeModule = "0xC93c8CDE0eDf4963ea1eea156099B285A945210a"
NavIssuanceModule = "0x5dB52450a8C0eb5e0B777D4e08d7A93dA5a9c848"

components = [usdcAddress]
units = [initialWethAmount]
modules = [BasicIssuanceModule, StreamingFeeModule, TradeModule, NavIssuanceModule]
manager = "0x3427A6cC667798339C471EC3c75a10e4A642306c"
name = "TEST USDC SET"
symbol = "TUS"


def deploy_token_set():
    account = get_account()

    stc = interface.ISetTokenCreator(
        config["networks"][network.show_active()]["contracts"]["SetTokenCreator"]
    )
    print(stc.address)
    add = stc.create(
        components, units, modules, manager, name, symbol, {"from": account}
    )
    print(add)
    return add


def main():
    deploy_token_set()
