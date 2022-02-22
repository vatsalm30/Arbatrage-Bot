const ownableFactory = artifacts.require('./Flashlaon.sol')

module.exports = async deployer => {
  await deployer.deploy(ownableFactory)
}
