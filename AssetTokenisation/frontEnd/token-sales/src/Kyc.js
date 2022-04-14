import web3 from './web3';
import contracts from './importFromBrownie/map.json';
import abi from './importFromBrownie/KycContract.json';
const Address = contracts["42"]["KycContract"][0];
const Abi = abi["abi"];

export default new web3.eth.Contract(Abi, Address);