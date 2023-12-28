'''
====================== CHECK MODE ======================
'''
# only check nft  !!! If True - === MINT MODE === needs to be configured !!!
CHECK_WALLET = False # True/False

'''
====================== MINT MODE ======================
'''
# RANDOM WALLETS MODE
RANDOM_WALLET = False  # True/False

# removing a wallet from the list after the job is done
REMOVE_WALLET = False # True/False

SLEEP_FROM = 1 # Second
SLEEP_TO = 6 # Second

# GWEI CONTROL MODE
CHECK_GWEI = True  # True/False
MAX_GWEI = 30

# RETRY MODE
RETRY_COUNT = 0

# GAS MODE
MAX_PRIORITY_FEE = {
    "ethereum": 0.01,
}

GAS_MULTIPLIER = 1.3
