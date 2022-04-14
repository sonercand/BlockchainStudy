import web3 from './web3';
import contracts from './importFromBrownie/map.json';
import abi from './importFromBrownie/Sales.json';
const salesAddress = contracts["42"]["Sales"][0];
const salesAbi = abi["abi"];

export default new web3.eth.Contract(salesAbi, salesAddress);