# Original question


# def process_transactions(transactions):
#     for t in transactions:
#         if t["type"] == "credit":
#             if t["amount"] > 0:
#                 print(f"Credit transaction of ${t['amount']}")
#             else:
#                 print("Invalid credit amount")
#         elif t["type"] == "debit":
#             if t["amount"] > 0:
#                 print(f"Debit transaction of ${t['amount']}")
#             else:
#                 print("Invalid debit amount")
#         else:
#             print("Unknown transaction type")


# transactions = [
#     {"type": "credit", "amount": 100},
#     {"type": "debit", "amount": 50},
#     {"type": "credit", "amount": -20},
#     {"type": "transfer", "amount": 30},
# ]

# Credit transaction of $100
# Debit transaction of $50
# Invalid credit amount
# Unknown transaction type
# process_transactions(transactions)

# refactored_code

def process_credit_transaction(transaction):
    if transaction["amount"] > 0:
        print(f"Credit transaction of ${transaction['amount']}")
    else:
        print("Invalid credit amount")


def process_debit_transaction(transaction):
    if transaction["amount"] > 0:
        print(f"Debit transaction of ${transaction['amount']}")
    else:
        print("Invalid debit amount")


def process_unknown_transaction(transaction):
    print("Unknown transaction type")


def process_transactions(transactions):
    transaction_handlers = {
        "credit": process_credit_transaction,
        "debit": process_debit_transaction,
    }

# Here I am passing Unknown in the case if type is not in transaction_handlers

    for transaction in transactions:
        handler = transaction_handlers.get(
            transaction["type"], process_unknown_transaction
        )
        handler(transaction)


transactions = [
    {"type": "credit", "amount": 100},
    {"type": "debit", "amount": 50},
    {"type": "credit", "amount": -20},
    {"type": "transfer", "amount": 30},
]

process_transactions(transactions)
