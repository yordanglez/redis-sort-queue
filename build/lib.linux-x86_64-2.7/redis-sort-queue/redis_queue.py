from redis import StrictRedis
import time
from datetime import datetime


class RedisQueue:
    def __init__(self, key):
        self.key = key
        self.redis = StrictRedis()

    def push(self, *args, **kwargs):
        if kwargs.has_key('is_date') and kwargs['is_date']:
            temp = ()
            for i, val in enumerate(args):
                if i % 2 == 0:
                    temp += (time.mktime(args[i].timetuple()),args[i+1],)
            args=temp
        self.redis.zadd(self.key, *args)

    def pop(self):
        range = self.redis.zrange(self.key, 0, 0)
        item = None
        if len(range):
            item = range[0]
            self.redis.zrem(self.key, item)

        return item

    def list(self, start=0, end=-1):
        return self.redis.zrange(self.key, start, end)

    def clean(self):
        self.redis.flushall()

#
# queue = RedisQueue('A')
# timestamp = time.time()
# now = datetime.fromtimestamp(timestamp)
# # queue.push(datetime.now(), "E",datetime.now(), "L", is_date=True)
# list= queue.list()
# print "goooo"
