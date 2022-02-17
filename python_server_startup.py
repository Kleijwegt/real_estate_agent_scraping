#! /usr/bin/python3
# Startup file for a python server, to host the excel file for access via my home network. Called at startup of the computer hosting these scripts.

import http.server
import socketserver
import os
os.chdir("/home/Desktop/house_data")

PORT = 9000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving a python server at port", PORT)
    httpd.serve_forever()