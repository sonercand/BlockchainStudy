import React from "react";
import './App.css';
import web3 from "./web3.js";
import SafeToken from './SafeToken.js';
import map from './importFromBrownie/map.json';
import Sales from './Sales.js';
import Kyc from './Kyc.js';
web3.eth.getAccounts(console.log);
class App extends React.Component {

  state = {
    manager: '',
    tokenName: '',
    totalSupply: '',
    salesRate: '',
    saleAddress: '',
    balance: '',
    tokenBalance: '',
    tokenAddress: '',
    kycAddress: "0x123...."
  }


  async componentDidMount() {


    const manager = await SafeToken.methods.owner().call();

    const tokenName = await SafeToken.methods.name().call();

    const totalSupply = await SafeToken.methods.totalSupply().call();
    const balance = await web3.eth.getBalance(web3.currentProvider.selectedAddress);
    const tokenBalance = await SafeToken.methods.balanceOf(web3.currentProvider.selectedAddress).call();
    const tokenAddress = map["42"]["SafeToken"][0];
    const salesRate = await Sales.methods.rate_().call();
    const saleAddress = '0xF9bb5b09079662dA009D85e9405174F1f150701c';
    this.listenToTokenTransfer();
    this.setState({ balance, manager, tokenName, totalSupply, tokenBalance, tokenAddress, salesRate, saleAddress }, this.updateUserTokens);

  };

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    this.setState({ [name]: value })
  };
  handleKycWhiteListing = async (event) => {
    event.preventDefault();
    const accounts = await web3.eth.getAccounts();
    await Kyc.methods.setKycCompleted(this.state.kycAddress).send({ from: accounts[0] });
  };
  updateUserTokens = async () => {
    let userTokens = await SafeToken.methods.balanceOf(web3.currentProvider.selectedAddress).call();
    this.setState({ userTokens: userTokens });
  };
  listenToTokenTransfer = async () => {
    SafeToken.events.Transfer({ to: web3.currentProvider.selectedAddress }).on("data", this.updateUserTokens);
  };
  handleBuyTokens = async (event) => {
    event.preventDefault();
    await Sales.methods.buyTokens(web3.currentProvider.selectedAddress).send({ from: web3.currentProvider.selectedAddress, value: 10 });
    const tokenBalance = await SafeToken.methods.balanceOf(web3.currentProvider.selectedAddress).call();
    const balance = await web3.eth.getBalance(web3.currentProvider.selectedAddress);
    this.setState({ tokenBalance, balance })

  };


  render() {
    return (
      <div class='row'>
        <div class='col'>
          <div class="jumbotron">
            <h2>Read from chain</h2>
            <hr />
            <p>SafeToken Contract address: {this.state.tokenAddress} - <a href='https://kovan.etherscan.io/address/0x121E45ae23d1C34eC119824B86814c58BE0d8Dc3' rel="noreferrer" target='_blank'>Check on etherscan</a>
            </p>
            <p>{this.state.tokenName} Contract managed by {this.state.manager}</p>
            <p>Total Supply: {web3.utils.fromWei(this.state.totalSupply)} </p>
            <p>Sales Contract Rate: 1 token for 10 wei</p>
            <p>Your ether balance: {web3.utils.fromWei(this.state.balance)} ether</p>
            <p> Your token balance: {web3.utils.fromWei(this.state.tokenBalance)}</p>
            <p> <p>Token sale address : {this.state.saleAddress} <a href='https://kovan.etherscan.io/address/0xF9bb5b09079662dA009D85e9405174F1f150701c' rel="noreferrer" target='_blank'>Check on etherscan</a></p></p>
          </div>
        </div>
        <div class='col'>
          <div class="jumbotron">
            <h2>Write to chain</h2>
            <hr />
            <h3>Allow address </h3>
            Address to allow: <input class="form-control" type="text" name="kycAddress" value={this.state.kycAddress} onChange={this.handleInputChange} />
            <button class='btn btn-primary btn-lg' type="button" onClick={this.handleKycWhiteListing}>Allow</button> # ONLY the Owner of the contract can run this.



            <p>currently you have {web3.utils.fromWei(this.state.tokenBalance)} tokens</p>
            <p>Buy one token</p>
            <p><button class='btn btn-primary btn-lg' type="button" onClick={this.handleBuyTokens}>Buy One Token</button></p>
          </div>
        </div>
      </div>

    )
  }
};


export default App;
