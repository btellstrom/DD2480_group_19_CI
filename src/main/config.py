import configparser
from os.path import abspath

"""The github api-token to be used for the CI-service"""
api_token = ''

"""The name of the mongo database"""
mongo_database_name = ''
"""Ip-address of the mongo database"""
mongo_ip = ''
"""Port number of the mongo database"""
mongo_port = ''
"""The username of the mongo database"""
mongo_user = ''
"""Password for above user of the mongo database"""
mongo_pass = ''

def init(conf_file = None):
    """
    Initialize the configuration and give values to the global variables
    specified above
    """
    global api_token
    global mongo_database_name
    global mongo_ip
    global mongo_port
    global mongo_user
    global mongo_pass
    
    config = configparser.ConfigParser()
    
    # This is only here for none dev purposes, this should never be used in dev
    if conf_file == None:
        config.read(abspath("../ci.ini"))
    else:
        config.read(conf_file)

    api_token = config['Notification']['api_token']

    mongo_database_name = config['Database']['name']
    mongo_ip = config['Database']['ip']
    mongo_port = config['Database']['port']
    mongo_user = config['Database']['user']
    mongo_pass = config['Database']['password']

