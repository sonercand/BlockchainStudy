// contracts/TestToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TestToken1 is ERC20 {
    constructor(uint256 initialSupply) ERC20("TestToken1", "TST1") {
        _mint(msg.sender, initialSupply);
    }
}
