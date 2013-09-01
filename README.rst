AtomicLong
==========

Sometimes you need to increment some numbers
... atomically
... in python.

``AtomicLong`` was born out of the need for fast thread-safe counters in python.

It uses `CFFI`_ to bind `GCC's Atomic Builtins`_.

It's value is a C ``long`` which can be incremented, decremented, and set
atomically.  It is inspired by Java's `java.util.concurrent.atomic.AtomicLong`_.

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
    >>> a -= 100
    >>> a.value
    900


.. _GCC's Atomic Builtins: http://gcc.gnu.org/onlinedocs/gcc-4.3.5/gcc/Atomic-Builtins.html

.. _CFFI: https://cffi.readthedocs.org

.. _java.util.concurrent.atomic.AtomicLong: http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/atomic/AtomicLong.html
