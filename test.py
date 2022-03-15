import hashlib

pw1 = 'goldvedio15769'
pw2 = 'goldvedio15769'
en_pw1 = hashlib.sha256(pw1.encode()).hexdigest()
en_pw2 = hashlib.sha256(pw2.encode()).hexdigest()
check = en_pw1 == en_pw2

print(check)