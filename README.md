# redis-sort-queue

redis-sort-queue is a priority queue for easy use on redis

Installation
------------
The easiest way to install the redis-sort-queue package is either via pip:

```
$ pip install redis-sort-queue
```

or manually by downloading the source and run the setup.py script:

```
$ python setup.py install
```

Examples
--------
We have put some self-explanatory examples in the [examples](https://github.com/yordanglez/redis-sort-queue/tree/master/example) directory, but here is a quick example on how to get started. Assuming the installation was successful, you can import the redis-sort-queue package like this:

```python
from redis_sort_queue.redis_queue import RedisQueue
```

Then, create an instance of **RedisQueue**:

```python
queue = RedisQueue('name_queue')
```

queue.push(100, "element1",1, "elment2")
element=queue.pop()
