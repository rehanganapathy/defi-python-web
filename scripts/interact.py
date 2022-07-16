import os
from brownie import Contract, accounts
from dotenv import load_dotenv
load_dotenv()

def main():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    usdc_contract = Contract('0x4A526f3Ba00D2b40D6BbB1c3C225A74a0aa32dE7')
    defi_contract = Contract('0x64944C8c6c4f7Ac0B276c482d456E43CA79A71A3')
    
    print(f"Before function call Current usdc token deposit balance is {defi_contract.depositBalance(account)}")
    usdc_contract.approve(defi_contract, 10000, {"from": account})
    defi_contract.depositToken(10000, {"from": account})

    print(f"After function call Current usdc token deposit balance is {defi_contract.depositBalance(account)}")
    
    defi_contract.withdraw(100, {"from": account})
    

    print(f"Current balance after Withdraw usdc token deposit balance is {defi_contract.depositBalance(account)}")
