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
queue.push(100, "element1",1, "element2")
element=queue.pop()
```

API library
------------

Methods defined here:

```__init__(self, key, **kwargs)```

```clean(self)```
    Delete all values in queue

```count(self)```
    Return the number of elements in the queue

```count_lex(self, min, max)```
    Return the number of items in the queue between the
    lexicographical range ``min`` and ``max``.

```count_priority(self, min, max)```
    Returns the number of elements in the queue with
    a score between ``min`` and ``max``.

```incr_priority(self, value, amount=1)```
    Increment the score of ``value`` in queue by ``amount``

```list(self, start=0, end=-1, desc=False, withscores=False, score_cast_func=<type 'float'>)```
    Return a range of values from queue between
    ``start`` and ``end`` sorted in ascending order.
     
    ``start`` and ``end`` can be negative, indicating the end of the range.
     
    ``desc`` a boolean indicating whether to sort the results descendingly
     
    ``withscores`` indicates to return the scores along with the values.
    The return type is a list of (value, score) pairs
     
    ``score_cast_func`` a callable used to cast the score return value

```list_by_lex(self, min, max, start=None, num=None)```
    Return the lexicographical range of values from sorted queue
    between ``min`` and ``max``.
     
    If ``start`` and ``num`` are specified, then return a slice of the
    range.

```list_by_priority(self, min, max, start=None, num=None, withscores=False, score_cast_func=<type 'float'>)```
    Return the lexicographical range of values from sorted queue
    between ``min`` and ``max``.
     
    If ``start`` and ``num`` are specified, then return a slice of the
    range.

```pop(self, desc=False)```
    Remove the first member ``values`` from queue ordered ``desc``

```push(self, *args, **kwargs)```
    Set any number of score, element-name pairs to the queue. Pairs
    can be specified in two ways:
     
    As *args, in the form of: score1, name1, score2, name2, ...
    or as **kwargs, in the form of: name1=score1, name2=score2, ...
     
    The following example would add four values to the 'my-key' key:
    redis.push( 1.1, 'name1', 2.2, 'name2', name3=3.3, name4=4.4)

```remove(self, *values)```
    Remove member ``values`` from queue

