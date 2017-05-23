from redis import StrictRedis
import time
from datetime import datetime


class RedisQueue:
    def __init__(self, key,**kwargs):
        self.key = key
        self.redis = StrictRedis(**kwargs)

    def push(self, *args):
        """
        Set any number of score, element-name pairs to the queue. Pairs
        can be specified in two ways:

        As *args, in the form of: score1, name1, score2, name2, ...

        The following example would add two values to the queue:
        redis.push( 1.1, 'name1', 2.2, 'name2')
        """

        temp = ()
        for i, val in enumerate(args):
            if i % 2 == 0 :
                if isinstance(val,datetime):
                    temp += (time.mktime(args[i].timetuple()),args[i+1],)
                else :
                    temp +=(args[i],args[i+1],)

        args=temp
        return self.redis.zadd(self.key, *args)

    def pop(self,desc=False):
        "Remove the first member ``values`` from queue ordered ``desc``"
        range = self.redis.zrange(self.key, 0, 0,desc)
        item = None
        if len(range):
            item = range[0]
            self.redis.zrem(self.key, item)
        return item

    def remove(self,*values):
        "Remove member ``values`` from queue"
        return self.redis.zrem(self.key, item,*values)



    def list(self, start=0, end=-1, desc=False, withscores=False,
               score_cast_func=float):
        """
        Return a range of values from queue between
        ``start`` and ``end`` sorted in ascending order.
        
        ``start`` and ``end`` can be negative, indicating the end of the range.
        
        ``desc`` a boolean indicating whether to sort the results descendingly
        
        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs
        
        ``score_cast_func`` a callable used to cast the score return value
        """
        return self.redis.zrange(self.key, start, end, desc,withscores,score_cast_func)

    def clean(self):
        "Delete all values in queue"
        len=self.count()
        items= self.list()
        for item in items:
            self.redis.zrem(self.key, item)
        return len

    def count(self):
        "Return the number of elements in the queue"
        return self.redis.zcard(self.key)

    def count_priority(self,min,max):
        """
        Returns the number of elements in the queue with
        a score between ``min`` and ``max``.
        """
        return self.redis.zcount(self.key,min,max)

    def incr_priority(self,value,amount=1):
        "Increment the score of ``value`` in queue by ``amount``"
        return self.redis.zincrby(self.key, value, amount)

    def count_lex(self,min,max):
        """
        Return the number of items in the queue between the
        lexicographical range ``min`` and ``max``.
        """
        return self.redis.zlexcount(self.key,min,max)


    def list_by_lex(self,min, max, start=None, num=None):
        """
        Return the lexicographical range of values from sorted queue
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.
        """
        return self.redis.zrangebylex(self.key,min, max, start=None, num=None)

    def list_by_priority(self, min, max, start=None, num=None,
                      withscores=False, score_cast_func=float):
        """
        Return the lexicographical range of values from sorted queue
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.
        """
        return self.redis.zrangebyscore(self.key, min, max, start, num,
                      withscores, score_cast_func)





