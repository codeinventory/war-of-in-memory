#!/usr/bin/env python

import redis
import time 
import pylibmc 
import random

def timeit(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

r_server = redis.Redis('localhost') #this line creates a new Redis object and
mc = pylibmc.Client(["127.0.0.1"])

def rand():
	return str(random.randint(0,100))

@timeit
def set_test_mc():
	mc.set(rand(), "Some value")


@timeit
def get_test_mc():
	mc.get(rand())


@timeit
def set_test_r():
	r_server.hset("12345",rand(), 'test_value') #with the created redis object we can

@timeit	
def get_test_r():
	r_server.hget("12345",rand())

for i in range(0,1000):
	set_test_mc()
for i in range(0,1000):
	set_test_r()

for i in range(0,1000):
	get_test_mc()
for i in range(0,1000):
	get_test_r()

