import json

with open('data/rpc.json') as file:
    RPC = json.load(file)

with open('data/abi/erc20_abi.json') as file:
    ERC20_ABI = json.load(file)

with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]

with open("data/abi/nft-origins/abi.json", "r") as file:
    NFT_ORIGINS_ABI = json.load(file)

NFT_ORIGINS_CONTRACT = "0x74670A3998d9d6622E32D0847fF5977c37E0eC91"

SCROLL_TOKENS = {
    "ETH": "0x5300000000000000000000000000000000000004",
    "WETH": "0x5300000000000000000000000000000000000004",
    "USDC": "0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4"
}
