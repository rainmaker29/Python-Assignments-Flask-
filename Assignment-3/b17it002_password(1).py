
import re
import bcrypt
import json

email = input()
password = input()

if bool(re.match("(^[a-z])([a-z0-9]+)@gmail\.com",email)):
    print("email works")
else:
    print("Change email")

if bool(re.compile('[A-Z]+').search(password)) and bool(re.compile('[a-z]+').search(password)) \
and bool(re.compile('[0-9]+').search(password)) and bool(re.compile('[!@#$%^&*=-]+').search(password)):
    print("Done")
else:
    print("Password Denied")
    password=None

salt = bcrypt.gensalt()
password = bytes(password,'utf-8')
hashed = bcrypt.hashpw(password, salt)

result = {
    'key':email,
    'hash':str(hashed)
}

with open('file.json','w') as f:
    f.write(json.dumps(result))
