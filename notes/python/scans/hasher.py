#!/usr/bin/python

import hashlib

hashvalue = input("* Enter a string to hash: ")

hashob1 = hashlib.md5()
hashob1.update(hashvalue.encode())
print("Md5: " + hashob1.hexdigest())

hashob2 = hashlib.sha1()
hashob2.update(hashvalue.encode())
print("Sha1: " + hashob2.hexdigest())

hashob3 = hashlib.sha224()
hashob3.update(hashvalue.encode())
print("Sha224: " + hashob3.hexdigest())

hashob4 = hashlib.sha256()
hashob4.update(hashvalue.encode())
print("Sha256: " + hashob4.hexdigest())

hashob5 = hashlib.sha512()
hashob5.update(hashvalue.encode())
print("Sha512: " + hashob5.hexdigest())