// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IIssuerModule {
    function issue(
        address _setToken,
        uint256 _quantity,
        address _to
    ) external;
}
