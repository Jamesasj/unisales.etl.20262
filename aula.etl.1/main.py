import requests
# Data acquisition
res = requests.get('https://jsonplaceholder.typicode.com/users')
users = res.json()

i = 0

for obj in users:
    print(i, obj['name'])
    i += 1