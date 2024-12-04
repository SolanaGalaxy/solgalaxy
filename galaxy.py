from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.transaction import Transaction, AccountMeta
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.keypair import Keypair
import base64

# Initialize the Solana client
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC_URL)

# Configuration (replace with your actual details)
GALAXY_AI_PROGRAM_ID = PublicKey("ReplaceWithYourProgramID")
GALAXY_AI_TOKEN_MINT = PublicKey("ReplaceWithYourTokenMint")
DEV_WALLET = PublicKey("ReplaceWithYourDeveloperWallet")

# Function to fetch account information
def get_account_info(account_address):
    account_info = client.get_account_info(account_address)
    if account_info["result"]["value"]:
        print("Account data:", account_info["result"]["value"]["data"])
        return account_info["result"]["value"]
    else:
        print("Account not found!")
        return None

# Function to create and send a transaction
def send_tokens(payer: Keypair, recipient: PublicKey, amount: int):
    # Create transfer instruction
    transfer_instruction = transfer(
        TransferParams(from_pubkey=payer.public_key, to_pubkey=recipient, lamports=amount)
    )

    # Create and sign transaction
    transaction = Transaction()
    transaction.add(transfer_instruction)
    try:
        response = client.send_transaction(transaction, payer, opts=TxOpts(skip_preflight=True))
        print("Transaction successful! Signature:", response["result"])
    except Exception as e:
        print("Transaction failed:", e)

# Example: Fetch account data
def example_fetch_account_data():
    example_account = PublicKey("ReplaceWithAnExampleAccount")
    account_data = get_account_info(example_account)
    if account_data:
        print("Fetched account data:", account_data)

# Example: Send tokens
def example_send_tokens():
    # Load payer's keypair (replace with your private key or wallet file)
    payer = Keypair()
    recipient = PublicKey("ReplaceWithRecipientAddress")
    amount = 1000000000  # Amount in lamports (1 SOL = 10^9 lamports)
    send_tokens(payer, recipient, amount)

if __name__ == "__main__":
    print("Galaxy AI - Solana Interaction Script")
    # Uncomment the operation you want to run
    # example_fetch_account_data()
    # example_send_tokens()
