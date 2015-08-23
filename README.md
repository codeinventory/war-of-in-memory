# war-of-in-memory
Benchmarking of different in memory databases

```bash
amey@xps ~/work/python/war-of-in-memory $ time ./memory-n-speed-test.py redis-normal

91858904 bytes, 87 MB

real	3m7.623s
user	2m13.062s
sys	0m38.274s

amey@xps ~/work/python/war-of-in-memory $ time ./memory-n-speed-test.py redis-hashes

17364880 bytes, 16 MB

real	3m52.364s
user	2m33.555s
sys	0m41.110s

amey@xps ~/work/python/war-of-in-memory $ time ./memory-n-speed-test.py memcached

54574019 bytes, 52 MB

real	1m29.610s
user	0m30.420s
sys	0m31.517s
```

#results 
on the performance, no one can beat the memcache, while redis is good at memory saving.

*"memory is inversely proportional to performance"* - *Amey*
