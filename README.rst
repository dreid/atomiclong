AtomicLong
==========

Sometimes you need to increment some numbers
… atomically
… in python.


``AtomicLong`` was born out of the need for fast thread-safe counters in python.

Example::

    >>> from atomiclong import AtomicLong
    >>> a = AtomicLong(0)
    >>> a += 1
    >>> a.value
    1
    >>> a += 10
    >>> a.value
    11
    >>> a.value = 1000
    >>> a.value
    1000
    >>> a.value -= 100
    >>> a.value
    900
