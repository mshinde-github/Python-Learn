import requests

req = requests.get("www.google.com");
content = req.json();
print(content);

for item in content['items']:
    print(item['name']);
    print(item['description']);
