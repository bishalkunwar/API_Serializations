import requests
import json

URL="http://127.0.0.1:8000/stud_get/"

def get_data(id = None):
    data = {}
    if id is not None:
        data={'id':id}
    json.dumps(data)
    req = requests.get(url=URL, data = data)
    data = req.json()
    print(data)

get_data(1)

def post_data():
    data = {
        'name':'raju',
        'number':458,
        'email':'emails@raju.com'
    }

    json_data = json.dumps(data)
    req = requests.post(url=URL, data = data)
    data = req.json()
    print(data)

post_data()

def update_data():
    data = {
        'id':4
        'name':'mithileshwor',
        'number':458,
        'email':'mitheleshwor@gmail.com'
    }

    json_data = json.dumps(data)
    req = requests.put(url=URL, data = data)
    data = req.json()
    print(data)

update_data()

def delete_data():
    data = {
        'id':1
        
    }

    json_data = json.dumps(data)
    req = requests.delete(url=URL, data = data)
    data = req.json()
    print(data)

delete_data()
