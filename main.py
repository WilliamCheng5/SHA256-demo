import random as rand
# ----------------------Creating all transactions---------------------- #
def generate_transaction():
    # create the Raw Transaction Hex String for each transaction as well, in the hexadecimal and little endian:
    transaction = 0x0
    # 4 byte version (assume version 2 0x02000000)
    transaction += 0x2
    # transaction inputs
    #       - 1 byte transaction count (assume 0x01)
    transaction += 0x1 << 4*8
    #       - 32 byte transaction ID (TXID, randomly generated for demo)
    transaction += rand.randint(0, 2**256-1) << 5*8
    #       - 4 byte index of previous transaction (randomly generated demo, 0-10)
    transaction += rand.randint(0, 10) << 37*8
    #       - 1 byte length of scriptSig (always 100)
    transaction += 0x64 << 41*8
    #       - 100 byte scriptSig (legacy P2PKH, for simplicity, randomly generated for demo)
    transaction += rand.randint(0, 2**800-1) << 42*8
    #       - 4 byte sequence number (assume no special sequence behavior, hence 0xffffffff)
    transaction += 0xffffffff << 142*8
    # transaction outputs
    #       - 1 byte number of outputs (randomly generated for demo, 1-5)
    output_count = rand.randint(1, 5)
    transaction += output_count << 146*8

    offset = 147
    for i in range(output_count):
        #       - 8 byte output bitcoin value (in satoshis, randomly generated, 0-1,000,000,000 or 0-10BTC)
        transaction += rand.randint(0, 1000000000) << offset*8
        offset += 8
        #       - 1 byte locking script length (alwaays 25 in this demo)
        transaction += 0x19 << offset*8
        offset += 1
        #       - 25 byte Bitcoin locking script (P2PKH, randomly generated for demo)
        transaction += rand.randint(0, 2**200-1) << offset*8
        offset += 25
    # 4 byte locktime (assume 0x00000000, so transaction is immediately valid)
    transaction += 0
    offset += 4

    return transaction
    print(transaction.to_bytes(offset, byteorder='little').hex())

# generate 500 transactions
transactions = []
for i in range(500):
    transactions.append(generate_transaction())
print(transactions[:10])
# ----------------------Hashing all individual transactions---------------------- #
