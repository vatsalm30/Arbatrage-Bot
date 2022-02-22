// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

/* solium-disable mixedcase */
contract Migrations {
    address public owner;
    uint256 public last_completed_migration;

    modifier restricted() {
        if (msg.sender == owner) _;
    }

    constructor() public {
        owner = msg.sender;
    }

    function setCompleted(uint256 completed) public restricted {
        last_completed_migration = completed;
    }

    function upgrade(address _newAddress) public restricted {
        Migrations upgraded = Migrations(_newAddress);
        upgraded.setCompleted(last_completed_migration);
    }
}

/* solium-enable mixedcase */
