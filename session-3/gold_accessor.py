    
class GoldAccessor:

    @staticmethod
    def get_gold_rates():
        # Get gold rates from third party API
        return 1, "Success", {"gold_prices": {}, "taxes": {}}