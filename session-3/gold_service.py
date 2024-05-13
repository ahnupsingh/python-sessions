
# API - views / Controller -> class , function
# Service - Class - Business logics 
    # GoldService - [Gold buy, sell, price]
# Accessor - Class - Get data from external API
# Helpers - Class
# Utils - function

import json
from utils.logger import logging as logger
from .redis_service import RedisService
from django.conf import settings
from .gold_accessor import GoldAccessor

class GoldService:

    def __init__(
        self,
        user=None,
    ):
        self.cache = RedisService.get_instance()
        self.user = user

    @staticmethod
    def get_metal_prices():
        logger.info('Updating prices for gold and silver.')

        status, message, response = GoldAccessor.get_gold_rates()
        if status != 1:
            return 0, message, {}

        gold_prices = response['gold_prices']
        taxes = response['taxes']
        _, _, response = GoldService.update_metal_prices(gold_prices, taxes)

        return 1, 'Successfully updated prices of gold/silver.', response
    
    @staticmethod
    def update_metal_prices(gold_prices, taxes):

        GST = 0.13
        gold_prices["gst"] = GST * 100

        redis = RedisService.get_instance()
        redis.set("gold_prices", json.dumps(gold_prices),
                  timeout=settings.GOLD_PRICE_REFRESH_INTERVAL)
        redis.set("gold_taxes", json.dumps(taxes), timeout=settings.GOLD_PRICE_REFRESH_INTERVAL)
        logger.info("Gold prices updated to {}".format(gold_prices))
        logger.info("Gold taxes updated to {}".format(gold_prices))

        return 1, "Success", {}


    def get_gold_price(self):
        prices = self.cache.get("gold_prices")
        if prices:
            logger.info("Returning cached gold prices")
            return 1, "Cached gold prices", json.loads(prices)

        status, message, prices = GoldService.get_metal_prices()
        if status != 1:
            logger.info("Returning fresh gold prices")
            return 0, message, {}

        return 1, message, prices
