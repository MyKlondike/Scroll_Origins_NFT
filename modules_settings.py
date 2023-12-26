import asyncio
import time

from modules import *

async def nft_origins(account_id, key):
    nft = NftOrigins(account_id, key)
    await nft.mint()

async def check_nft_origins(account_id, key):
    check = NftOrigins(account_id, key)
    await check.checker_nft()
