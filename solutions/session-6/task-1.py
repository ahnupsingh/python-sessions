def process_credit_transaction(amount):
    if amount > 0:
        print(f"Credit transaction of ${amount}")
    else:
        print("Invalid credit amount")

def process_debit_transaction(amount):
    if amount > 0:
        print(f"Debit transaction of ${amount}")
    else:
        print("Invalid debit amount")

def process_transaction(transaction):
    transaction_type = transaction['type']
    amount = transaction['amount']
    
    transaction_handlers = {
        'credit': process_credit_transaction,
        'debit': process_debit_transaction
    }
    
    handler = transaction_handlers.get(transaction_type)
    if handler:
        handler(amount)
    else:
        print("Unknown transaction type")

def process_transactions(transactions):
    for transaction in transactions:
        process_transaction(transaction)

transactions = [
    {'type': 'credit', 'amount': 100},
    {'type': 'debit', 'amount': 50},
    {'type': 'credit', 'amount': -20},
    {'type': 'transfer', 'amount': 30}
]