#!/usr/bin/env python3

import json
import os
import subprocess
from logging import info, error

import requests
from bs4 import BeautifulSoup

def open_text_editor(filename):
    if os.name == 'nt':
        # untested
        info('Opening Windows Notepad')
        subprocess.Popen(['notepad', filename]).wait()
    else:
        info('Opening Linux system editor')
        subprocess.Popen([os.environ['EDITOR'], filename]).wait()

def get_config_dict(filename):
    if not os.path.exists(filename):
        info('Configuraiton file does not exist. Returning None')
        return None
    info('Loading configuration into dictionary and returning')
    with open(filename, 'r') as f:
        return json.load(f)

def config_list(args):
    pass

def config_remove(args):
    pass

def config_add(args):
    pass

def config_open(args):
    pass

def run(args):
    print('test')
    pass

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Tool when run checks if a website changed a specific part and if yes send notifications. Aslo implements tools to change its own configuration')
    parser.add_argument('-c', '--config', default='config.json', help='Name of the config file in the same directory. Default: config.json')
    subparsers = parser.add_subparsers()

    parser_config = subparsers.add_parser('config', help='Choses config sub functions')
    subparsers_config = parser_config.add_subparsers()

    parser_config_list = subparsers_config.add_parser('list', help='List the names of all configurations')
    parser_config_list.set_defaults(func=config_list)

    parser_config_remove = subparsers_config.add_parser('remove', help='Remove the specified config')
    parser_config_remove.add_argument('name', help='Name of the config to be removed')
    parser_config_remove.set_defaults(func=config_remove)

    parser_config_add = subparsers_config.add_parser('add', help='Add the specified config')
    parser_config_add.add_argument('name', help='Name of the config to be added and then opened')
    parser_config_add.set_defaults(func=config_add)

    parser_config_open = subparsers_config.add_parser('open', help='Open the specified config')
    parser_config_open.add_argument('name', help='Name of the config to be opened for viewing or editing')
    parser_config_open.set_defaults(func=config_open)

    parser_run = subparsers.add_parser('run', help='Run tool with given configuration')
    parser_run.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)