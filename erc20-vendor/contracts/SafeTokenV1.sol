// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SafeTokenV1 is ERC20 {
    constructor(uint256 initialSupply) ERC20("Safe Token Version 1", "STV1") {
        _mint(msg.sender, initialSupply);
    }
}
