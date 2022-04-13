var SafeToken = artifacts.require("SafeToken.sol");

module.exports = async function (deployer) {
    await deployer.deploy(SafeToken);
}