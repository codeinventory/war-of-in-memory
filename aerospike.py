#!/usr/bin/env python
import aerospike as aero

config = {
  'hosts': [ ('localhost', 3000) ]
}
NUM_ENTRIES = 1000000
MAX_VAL = 12000000

try:
  client = aero.client(config).connect()
except:
  print "exception connecting to aerospike"
  import sys
  sys.exit(1)

key = ('test', 'demo', 'foo')

try:

	for i in range(0, NUM_ENTRIES):
    		value = random.randint(0, MAX_VAL)
    		client.put(str(i),{'value':str(value)})

except Exception as e:
  import sys


client.close()
