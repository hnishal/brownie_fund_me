from brownie import FundMe
from brownie.network import account
from scripts.helping_functions import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance Fee: {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("Successfully Transfered")


def main():
    fund()
    withdraw()
