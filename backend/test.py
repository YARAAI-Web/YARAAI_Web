import requests

url = 'http://localhost:5173/api/section'

param = {
    'sectionId' : 1,
    'filename' : 'd0f9b5c0-4511-4fa4-88d9-35833dc0e9fa'
}

r = requests.post(url, json=param)
print(r.text)