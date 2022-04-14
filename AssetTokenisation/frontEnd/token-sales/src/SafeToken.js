import web3 from './web3';
import contracts from './importFromBrownie/map.json';
import abi from './importFromBrownie/SafeTokenABI.json';
const safeTokenAddress = contracts["42"]["SafeToken"][0];
const safeTokenAbi = abi["abi"];

export default new web3.eth.Contract(safeTokenAbi, safeTokenAddress);
