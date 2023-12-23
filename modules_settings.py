import asyncio

async def nft_origins(account_id, key):
    nft = NftOrigins(account_id, key)
    await nft.mint()


def get_tx_count():
    asyncio.run(check_tx())
