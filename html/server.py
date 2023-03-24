import http.server
import socketserver
import os
from modules.commonData import *

pubFolder = root/"/public"

#because we can and i like it
PORT = 89_89
DIRECTORY = os.path.expanduser()

# specify the directory containing the HTML files
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

# set the working directory to the directory containing the HTML files
os.chdir(DIRECTORY)

print(f"Serving on port {PORT} from {DIRECTORY}")
httpd.serve_forever()