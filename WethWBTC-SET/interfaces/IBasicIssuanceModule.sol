// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import {ISetToken} from "./ISetToken.sol";

interface IBasicIssuanceModule {
    function getRequiredComponentUnitsForIssue(
        ISetToken _setToken,
        uint256 _quantity
    ) external returns (address[] memory, uint256[] memory);

    function initialize(address settoken, address preissuehook) external;

    function issue(
        address settoken,
        uint256 quantity,
        address _to
    ) external;
}
