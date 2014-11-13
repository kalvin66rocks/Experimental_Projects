import hashlib

def md5_hash():
	filename = 'md5_' + strength + '.txt'
	fo = open(filename, 'wb')
	with open(file_in) as f:
		for line in f:
			md5_hash = hashlib.md5(line).hexdigest()
			fo.write(md5_hash + '\n')
	fo.close()

def sha_hash():
	with open(file_in) as f:
		for line in f:
			sha_hash = hashlib.sha1(line).hexdigest()
			print sha_hash, len(sha_hash)

def sha224_hash():
	with open(file_in) as f:
		for line in f:
			sha224_hash = hashlib.sha224(line).hexdigest()
			print sha224_hash, len(sha224_hash)

def sha256_hash():
	with open(file_in) as f:
		for line in f:
			sha256_hash = hashlib.sha256(line).hexdigest()
			print sha256_hash, len(sha256_hash)

def sha384_hash():
	with open(file_in) as f:
		for line in f:
			sha384_hash = hashlib.sha384(line).hexdigest()
			print sha384_hash, len(sha384_hash)

def sha512_hash():
	with open(file_in) as f:
		for line in f:
			sha512_hash = hashlib.sha512(line).hexdigest()
			print sha512_hash, len(sha512_hash)








if __name__ =='__main__':
	file_in = 'pswd_ok.txt'
	strength = 'ok'
	md5_hash()
	sha_hash()
	#sha224_hash()
	sha256_hash()
	#sha384_hash()
	#sha512_hash()

