import transaction_generator

T_COUNT = 500 # number of transactions

# generate transactions
transactions = []
for i in range(T_COUNT):
    transactions.append(transaction_generator.generate_transaction())
print(transactions[:10])