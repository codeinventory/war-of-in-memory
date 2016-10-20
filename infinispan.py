import sys
from infinispan.remotecache import RemoteCache
import random

NUM_ENTRIES = 1000000
MAX_VAL = 12000000



def main():
	remote_cache = RemoteCache()
	for i in range(0, NUM_ENTRIES):
		value = random.randint(0, MAX_VAL)
		remote_cache.put(str(i),str(value))


if __name__ == "__main__":
   sys.exit(main())


