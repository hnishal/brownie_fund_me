from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helping_functions import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    # we have to pass pricefeed address to our contract while dploymetn

    # if we are on persistent network like rinkeby use associated adddress
    # else deply mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # publish_source is is used to verify and publish source code directly
    # you have to add ETHERSCAN_TOKE(api key) to dotenv
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()


# for development networks brownie dosent remember thier deployments
# to add this we have to add ganache to networks
# command to do so -> brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337
