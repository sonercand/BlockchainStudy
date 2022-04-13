// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./Crowdsale.sol";
import "./KycContract.sol";

contract Sales is Crowdsale {
    KycContract kyc;

    constructor(
        uint256 rate,
        address payable wallet,
        IERC20 token,
        KycContract _kyc
    ) public Crowdsale(rate, wallet, token) {
        kyc = _kyc;
    }

    function _preValidatePurchase(address beneficiary, uint256 weiAmount)
        internal
        view
        override
    {
        super._preValidatePurchase(beneficiary, weiAmount);
        require(
            kyc.kycCompleted(msg.sender),
            "KYV not completed, purchase not allowed"
        );
    }
}
