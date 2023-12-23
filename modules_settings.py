import asyncio
from modules import *

async def nft_origins(account_id, key):
    nft = NftOrigins(account_id, key)
    await nft.mint()
