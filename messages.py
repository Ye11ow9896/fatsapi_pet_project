import configparser
from enum import Enum


msg = configparser.ConfigParser()
msg.read('messages.ini')


class UserMessage(str, Enum):
    not_found = msg['user']['not_found']
    updated_success = msg['user']['updated_success']
    deleted_success = msg['user']['deleted_success']