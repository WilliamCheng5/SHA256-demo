import random as rand

# ----------------------Creating all transactions---------------------- #
def generate_transaction():
    transaction = bytearray()
    # 4 byte version (assume version 2 0x02000000)
    transaction += (2).to_bytes(4, "little")
    # transaction inputs
    #       - 1 byte transaction count (assume 0x01)
    transaction += (1).to_bytes(1, "little")
    #       - 32 byte transaction ID (TXID, randomly generated for demo)
    transaction += rand.randbytes(32)
    #       - 4 byte index of previous transaction (randomly generated demo, 0-10)
    transaction += (rand.randint(0, 10)).to_bytes(4, "little")
    #       - 1 byte length of scriptSig (always 100)
    transaction += (100).to_bytes(1, "little")
    #       - 100 byte scriptSig (legacy P2PKH, for simplicity, randomly generated for demo)
    transaction += rand.randbytes(100)
    #       - 4 byte sequence number (assume no special sequence behavior, hence 0xffffffff)
    transaction += (0xffffffff).to_bytes(4, "little")
    # transaction outputs
    #       - 1 byte number of outputs (randomly generated for demo, 1-5)
    output_count = rand.randint(1, 5)
    transaction += (output_count).to_bytes(1, "little")

    for i in range (output_count):
        #       - 8 byte output bitcoin value (in satoshis, randomly generated, 0-1,000,000,000 or 0-10BTC)
        transaction += (rand.randint(0, 1000000000)).to_bytes(8, "little")
        #       - 1 byte locking script length (alwaays 25 in this demo)
        transaction += (25).to_bytes(1, "little")
        #       - 25 byte Bitcoin locking script (P2PKH, randomly generated for demo, beginning and end follow standard structure)
        transaction += bytes.fromhex("76a914")
        transaction += rand.randbytes(20)
        transaction += bytes.fromhex("88ac")

    # 4 byte locktime (assume 0x00000000, so transaction is immediately valid)
    transaction += (0).to_bytes(4, "little")
    return transaction

