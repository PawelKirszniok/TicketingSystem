from configparser import ConfigParser


def verify_code(code: str) -> bool:

    config_object = ConfigParser()
    config_object.read("config.ini")

    key = config_object['KEYS']['secretkey']

    if code == key:
        return True
    else:
        return False