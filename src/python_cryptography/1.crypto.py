import hashlib

message = "Hello".encode('utf-8')

h = hashlib.md5()
h.update(message)
print(h.hexdigest())

h = hashlib.sha256()
h.update(message)
print(h.hexdigest())

# check - file checksum
salt = "salting".encode('utf-8')
h = hashlib.sha256()
h.update(message + salt)
print(h.hexdigest())


password = "aa2f2f5063354ff78bb68bf13b9225cdac22a5275f38d6699f058e4582acc514"
salt = "salting".encode('utf-8')
