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
    this.setState({ balance, manager, tokenName, totalSupply, tokenBalance, tokenAddress, salesRate });

  };

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    this.setState({ [name]: value })
  };
  handleKycWhiteListing = async () => {
    const accounts = await web3.eth.getAccounts();
    await Kyc.methods.setKycCompleted(this.state.kycAddress).send({ from: accounts[0] });
  };
  render() {
    return (
      <div>
        <div>
          <h2>Read from chain</h2>
          <p>SafeToken Contract address: {this.state.tokenAddress}</p>
          <br />
          <p>{this.state.tokenName} Contract managed by {this.state.manager}</p>
          <p>Total Supply: {web3.utils.fromWei(this.state.totalSupply)} </p>
        </div>
        <div>Sales Contract Rate: {this.state.salesRate} token per ether
          <p>balance: {web3.utils.fromWei(this.state.balance)} ether</p>
          <p> token balance: {web3.utils.fromWei(this.state.tokenBalance)}</p>
        </div>
        <div>
          <h2>Write to chain</h2>
          <hr />
          <h3>Allow address </h3>
          Address to allow: <input type="text" name="kycAddress" value={this.state.kycAddress} onChange={this.handleInputChange} />
          <button type="button" onClick={this.handleKycWhiteListing}>Allow</button> # ONLY the Owner of the contract can run this.
        </div>
      </div>
    )
  }
};


export default App;
