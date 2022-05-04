import json


def get_urls():
    with open('src/configs/urls.json') as f:
        return json.load(f)


def get_user():
    with open('src/configs/users.json') as f:
        users = json.load(f)
        for user in users.values():
            if user['status'] == 'available':
                return user
    return None


def get_script(name):
    with open('src/configs/scripts.json') as f:
        scripts = json.load(f)
        return scripts[name]


def get_elements(name):
    with open('src/configs/elements.json') as f:
        scripts = json.load(f)
        return scripts[name]
