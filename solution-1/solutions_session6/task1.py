# def process_transactions(transactions):
#         for t in transactions:
#             if t['type'] == 'credit':
#                 if t['amount'] > 0:
#                     print(f"Credit transaction of ${t['amount']}")
#                 else:
#                     print("Invalid credit amount")
#             elif t['type'] == 'debit':
#                 if t['amount'] > 0:
#                     print(f"Debit transaction of ${t['amount']}")
#                 else:
#                     print("Invalid debit amount")
#             else:
#                 print("Unknown transaction type")

# transactions = [
#     {'type': 'credit', 'amount': 100},
#     {'type': 'debit', 'amount': 50},
#     {'type': 'credit', 'amount': -20},
#     {'type': 'transfer', 'amount': 30}
# ]

# -------------------------------------------------------------------------------------------------------------------------------------
# Refactored Code

class TransactionService():
    """ Essential methods for transaction service """

    def execute_transaction(self, transaction: dict) -> None:
        if not self.is_credit_valid(transaction):
            return self.handle_invalid_credit_amount()

        type = transaction.get("type", "").lower()
        if type == 'credit':
            return self.credit(transaction)
        if type == 'debit':
            return self.debit(transaction)
        return self.handle_unknown_transaction_type()


    def execute_bulk_transactions(self, transactions: list[dict]) -> None:
        for transaction in transactions:
            self.execute_transaction(transaction)
    
    def credit(self, transaction: dict) -> bool:
        print(f"Credit transaction of ${transaction['amount']}")
        return True

    def debit(self, transaction: dict) -> bool:
        print(f"Debit transaction of ${transaction['amount']}")
        return True

    def is_credit_valid(self, transaction: dict) -> bool:
        if transaction.get('amount', 0) > 0:
            return True
        return False
    
    @staticmethod
    def handle_invalid_credit_amount() -> None:
        print("Invalid credit amount")
        return None

    @staticmethod
    def handle_unknown_transaction_type() -> None:
        print("Unknown Transaction Type")
        return None


service = TransactionService()
service.execute_bulk_transactions(transactions)
