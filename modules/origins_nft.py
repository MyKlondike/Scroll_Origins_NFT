import aiohttp
from loguru import logger
import csv

from config import NFT_ORIGINS_CONTRACT, NFT_ORIGINS_ABI
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class NftOrigins(Account):
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll")

        self.contract = self.get_contract(NFT_ORIGINS_CONTRACT, NFT_ORIGINS_ABI)

    async def get_nft_data(self):
        url = f"https://nft.scroll.io/p/{self.address}.json"

        async with aiohttp.ClientSession() as session:
            response = await session.get(url=url)

            if response.status == 200:
                transaction_data = await response.json()

                if "metadata" in transaction_data:
                    return transaction_data["metadata"], transaction_data["proof"]

        return False, False

    async def checker_nft(self):
        res = await self.contract.functions.balanceOf(self.address).call()
        logger.info(f"Check Scroll Origins NFT: {self.address} - {res}")

        csv_filename = "result.csv"

        with open(csv_filename, mode = 'a', newline = '') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['address', 'res'])
            writer.writerow([self.address, res])
            await asyncio.sleep(0.5)

        return res

    @retry
    @check_gas
    async def mint(self):
        logger.info(f"[{self.account_id}][{self.address}] Mint Scroll Origins NFT")

        metadata, proof = await self.get_nft_data()

        if not metadata or not proof:
            return logger.error(f"[{self.account_id}][{self.address}] Scroll Origins NFT Not Found")

        tx_data = await self.get_tx_data()

        transaction = await self.contract.functions.mint(
            self.address,
            (
                metadata.get("deployer"),
                metadata.get("firstDeployedContract"),
                metadata.get("bestDeployedContract"),
                int(metadata.get("rarityData", 0), 16),
            ),
            proof
        ).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())