// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ISafeTokenMarket {
    function buyTokens() external payable returns (uint256 tokenAmount);

    function sellTokens(uint256 tokenAmountToSell) external payable;
}
