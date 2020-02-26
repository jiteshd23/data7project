import configparser

_config = configparser.ConfigParser() #create object
_config.read('../config.ini')

def bucket():
    return _config['AWS']['bucket']

def driver():
    return _config['SQL-SERVER']['driver']

def server():
    return _config['SQL-SERVER']['server']

def database():
    return _config['SQL-SERVER']['database']

def username():
    return _config['SQL-SERVER']['username']

def password():
    return _config['SQL-SERVER']['password']

def driver():
    return _config['SQL-SERVER']['driver']
