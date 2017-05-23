redis-sort-queue
================

redis-sort-queue is a priority queue for easy use on redis

Installation
------------

The easiest way to install the redis-sort-queue package is either via
pip:

::

    $ pip install redis-sort-queue

or manually by downloading the source and run the setup.py script:

::

    $ python setup.py install

Examples
--------

We have put some self-explanatory examples in the
`examples <https://github.com/yordanglez/redis-sort-queue/tree/master/redis_sort_queue/example>`__
directory, but here is a quick example on how to get started. Assuming
the installation was successful, you can import the redis-sort-queue
package like this:

Then, create an instance of **RedisQueue**:

.. code:: python

    from redis_sort_queue import RedisQueue

.. code:: python

    queue = RedisQueue('name_queue')
    queue.push(100, "element1",1, "element2")
    element=queue.pop()

If you want to use multiple queues you must create an instance of
**CollectionQueues** :

.. code:: python

    from redis_sort_queue import RedisQueue, CollectionQueues

.. code:: python

    queue1 = RedisQueue('A')
    queue2 = RedisQueue('B')
    queue1.push(100, "E",1, "L")
    queue2.push(101, "T")

.. code:: python

    collection=CollectionQueues()
    queue3= collection.intersect_queues('intersect1',['A','B'])

If you want to use pool connection **ConnectionPool** :

.. code:: python

    from redis_sort_queue import RedisQueue, CollectionQueues, ConnectionPool

.. code:: python

    pool = ConnectionPool(host='127.0.0.1', port=6379)

.. code:: python

    queue1 = RedisQueue('A',connection_pool=pool)
    queue2 = RedisQueue('B',connection_pool=pool)
    queue1.push(100, "E",1, "L", is_date=True)
    queue2.push(101, "T",datetime.now(), 10, is_date=True)

    collection=CollectionQueues(connection_pool=pool)
    queue3= collection.intersect_queues('intersect1',['A','B'])
    element=queue.pop()

API library
-----------

Methods defined here:

| **clean** ``python clean(self)``
| Delete all values in queue

**count**

.. code:: python

    count(self)

Return the number of elements in the queue

**count\_lex**

.. code:: python

    count_lex(self, min, max)

Return the number of items in the queue between the lexicographical
range **min** and **max**.

**count\_priority**

.. code:: python

    count_priority(self, min, max)

Returns the number of elements in the queue with a score between **min**
and **max**.

| **incr\_priority** ``python incr_priority(self, value, amount=1)``
| Increment the score of **value** in queue by **amount**

**list**

.. code:: python

    list(self, start=0, end=-1, desc=False, withscores=False, score_cast_func=type float)

Return a range of values from queue between **start** and **end** sorted
in ascending order.

**start** and **end** can be negative, indicating the end of the range.

**desc** a boolean indicating whether to sort the results descendingly

**withscores** indicates to return the scores along with the values. The
return type is a list of (value, score) pairs

**score\_cast\_func** a callable used to cast the score return value

**list\_by\_lex**

.. code:: python

    list_by_lex(self, min, max, start=None, num=None)

Return the lexicographical range of values from sorted queue between
**min** and **max**.

If **start** and **num** are specified, then return a slice of the
range.

**list\_by\_priority**

.. code:: python

    list_by_priority(self, min, max, start=None, num=None, withscores=False, score_cast_func=<type 'float'>)

Return the lexicographical range of values from sorted queue between
**min** and **max**.

If **start** and **num** are specified, then return a slice of the
range.

**pop**

.. code:: python

    pop(self, desc=False)

Remove the first member **values** from queue ordered **desc**

**push**

.. code:: python

    push(self, *args, **kwargs)

Set any number of score, element-name pairs to the queue. Pairs can be
specified in two ways:

As \*args, in the form of: score1, name1, score2, name2, ...

The following example would add two values to the queue: redis.push(
1.1, 'name1', 2.2, 'name2')

**remove**

.. code:: python

    remove(self, *values)

Remove member values from queue
