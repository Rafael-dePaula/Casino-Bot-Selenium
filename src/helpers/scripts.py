from src.helpers import configs, regex as re


def sign_in(username=None, password=None):
    # ! Change for multiples users
    elements = configs.get_elements('login')
    return re.sub_map(configs.get_script('login'), **elements)


def check_login():
    elements = configs.get_elements('general')
    return re.sub_map(configs.get_script('check_login'), **elements)


def get_last_numbers():
    return configs.get_script('get_history_elements')


def remind_later():
    return configs.get_script('remind_later')
