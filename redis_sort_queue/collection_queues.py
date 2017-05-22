from redis import StrictRedis
from .redis_queue import RedisQueue

class CollectionQueues:
    def __init__(self, **kwargs):
        self.kwargs=kwargs
        self.redis = StrictRedis(**kwargs)


    def intersect_queues(self,dest,keys,aggregate=None):
        """
        Intersect multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.
        """
        self.redis.zinterstore(dest,keys,aggregate)
        return RedisQueue(dest,**self.kwargs)

    def union_queues(self,dest,keys,aggregate=None):
        """
        Union multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.
        """
        self.redis.zunionstore(dest,keys,aggregate)
        return RedisQueue(dest,**self.kwargs)


