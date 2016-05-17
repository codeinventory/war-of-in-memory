package com.codeinventory.aerospike;

import java.util.Random;

import com.aerospike.client.AerospikeClient;
import com.aerospike.client.Bin;
import com.aerospike.client.Key;
import com.aerospike.client.Record;

public class Aerospike {
	
	
	static int NUM_ENTRIES = 1000000;
	static int MAX_VAL = 12000000;

	
	public static void main(String ... args){
		AerospikeClient client = new AerospikeClient("127.0.0.1", 3000);

		long start = System.currentTimeMillis();
		
		for (int i=0;i<NUM_ENTRIES;i++ ){
		Key key = new Key("test", "demo", getRandomInt());
		Bin bin1 = new Bin("bin1", "value1");

		client.put(null, key, bin1);
		}
		//Record record = client.get(null, key);
		
		System.out.println((System.currentTimeMillis() - start)/1000);

		client.close();
	}
	static Random rand = new Random();
	public static int  getRandomInt(){
		
		int randomNum = 0 + rand.nextInt(MAX_VAL + 1);
		return randomNum;
	}

}
