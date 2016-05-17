# war-of-in-memory
Benchmarking of different in memory databases

## Redis
```bash
amey@xps ~/work/python/war-of-in-memory $ time ./memory-n-speed-test.py redis-normal

91858904 bytes, 87 MB

real	3m7.623s
user	2m13.062s
sys	0m38.274s
```

## Redis with hashes
```bash
amey@xps ~/work/python/war-of-in-memory $ time ./memory-n-speed-test.py redis-hashes

17364880 bytes, 16 MB

real	3m52.364s
user	2m33.555s
sys	0m41.110s
```

## Memcache
```bash
amey@xps ~/work/python/war-of-in-memory $ time ./memory-n-speed-test.py memcached

54574019 bytes, 52 MB

real	1m29.610s
user	0m30.420s
sys	0m31.517s
```

### Aerospike
```bash
amey@xps ~/work/java/workspace/speech $ time mvn exec:java -Dexec.mainClass="com.codeinventory.aerospike.Aerospike"
97 _(time syso)_

used-bytes-memory 85346016, 81 MB

real	1m46.096s
user	0m38.840s
sys	0m36.448s
```

#Results 
on the performance, no one can beat the memcache, while redis-hash is good at memory saving, on the penalty of time.

*"memory is inversely proportional to performance"* - *Amey*
