import redis
from ..setting import REDIS_HOST,REDIS_PORT,REDIS_KEY_UNCHECK_IP,REDIS_DB
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT,db=REDIS_DB)
red1 = redis.Redis(connection_pool=pool)