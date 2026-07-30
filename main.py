import transaction_generator
import sha256

T_COUNT = 500 # number of transactions

# generate transactions
transactions = []
for i in range(T_COUNT):
    transactions.append(transaction_generator.generate_transaction())
# print(transactions[:10])

sha256.sha256(transactions[0])