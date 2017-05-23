from redis_sort_queue import RedisQueue, CollectionQueues, ConnectionPool
import time
from datetime import datetime


pool = ConnectionPool(host='127.0.0.1', port=6379)
queue1 = RedisQueue('A',connection_pool=pool)
queue2 = RedisQueue('B',connection_pool=pool)

timestamp = time.time()
now = datetime.fromtimestamp(timestamp)
queue1.push(datetime.now(), "E",datetime.now(), "L")
queue2.push(datetime.now(), "T",datetime.now(), "C")
collection=CollectionQueues(connection_pool=pool)
queue3= collection.intersect_queues('intersect1',['A','B'])

print queue1.list()
print queue2.list()
print queue3.list()
