def process_transaction(transaction, type):
    if transaction["amount"] > 0:
        print(f"{type} transaction of ${transaction['amount']}")
    else:
        print(f"Invalid {type} amount")


def process_transactions(transactions):

    if not transactions:
        raise Exception("Transactions are empty.")

    if not isinstance(transactions, list):
        raise ValueError("Transactions must be a list")

    transaction_handler = {
        "credit": process_transaction,
        "debit": process_transaction,
    }
    for transaction in transactions:
        if (
            not transaction
            or not transaction.get("type")
            or not transaction.get("amount")
        ):
            raise Exception("Invalid transaction")

        handler = transaction_handler.get(transaction["type"])

        if not handler:
            raise Exception("Unknown transaction type")
        if handler:
            handler(transaction, transaction["type"])


transactions = [
    {"type": "credit", "amount": 100},
    {"type": "debit", "amount": 50},
    {"type": "credit", "amount": -20},
    {"type": "transfer", "amount": 30},
]

try:
    process_transactions(transactions)
except Exception as e:
    print(e)
