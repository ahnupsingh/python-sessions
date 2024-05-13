from django_redis import get_redis_connection

class RedisService:
    __instance = None

    def __init__(self):
        if RedisService.__instance is None:
            # Logic to connect to redis server
            self.__redis = get_redis_connection("default")
            RedisService.__instance = self
        else:
            raise Exception("Can't create more than one instances")

    # Singleton pattern
    @staticmethod
    def get_instance():
        if RedisService.__instance is None:
            return RedisService()
        return RedisService.__instance

    def get(self, key):
        value = self.__redis.get(key)
        if value:
            return value.decode()
        return value

    def set(self, key, value, timeout):
        return self.__redis.set(key, value, int(timeout))

    def update(self, key, value, timeout=None):
        if self.__redis.exists(key):
            self.__redis.set(key, value, timeout)

    def delete(self, key):
        self.__redis.delete(key)

    def get_all_hash(self, key):
        return self.__redis.hgetall(key)

    def set_hash(self, key, hashmap):
        self.__redis.hmset(key, hashmap)

    def del_keys(self, key, *ids):
        if ids:
            self.__redis.hdel(key, *ids)
