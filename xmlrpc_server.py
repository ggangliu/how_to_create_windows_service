# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:35:27 2019

@author: 刚刚刘
"""

from xmlrpc.server import SimpleXMLRPCServer

from pysc import event_stop


class TestServer:

    def echo(self, msg):
        return msg


if __name__ == '__main__':
    server = SimpleXMLRPCServer(('127.0.0.1', 9001))

    @event_stop
    def stop():
        server.server_close()

    server.register_instance(TestServer())
    server.serve_forever()