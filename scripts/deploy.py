import os
from brownie import accounts, USDC, RUSD, DefiBank
from dotenv import load_dotenv
load_dotenv()

def main():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    usdc_addr = USDC.deploy({"from": account})
    rusd_addr = RUSD.deploy({"from": account})
    DefiBank.deploy(usdc_addr, rusd_addr, {"from": account})