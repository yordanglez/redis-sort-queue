from redis_sort_queue.redis_queue import RedisQueue
import time
from datetime import datetime



queue = RedisQueue('A')
timestamp = time.time()
now = datetime.fromtimestamp(timestamp)
# queue.push(datetime.now(), "E",datetime.now(), "L", is_date=True)
list= queue.list()
print "goooo"
