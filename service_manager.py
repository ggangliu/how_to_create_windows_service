# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:37:43 2019

@author: 刚刚刘
"""

import os
import sys
from xmlrpc.client import ServerProxy

import pysc


if __name__ == '__main__':
    command = sys.argv[1]
    
    service_name = 'xmlrpc_server'
    script_path = os.path.join(
        os.path.dirname(__file__), 'xmlrpc_server.py'
    )
    pysc.create(
        service_name=service_name,
        cmd=[sys.executable, script_path]
    )
    
    if 'start' == command:
        pysc.start(service_name)
        client = ServerProxy('http://127.0.0.1:9001')
        print(client.echo('test scm'))
    elif 'stop' == command:
        pysc.stop(service_name)
    elif 'delete' == command:
        pysc.delete(service_name)