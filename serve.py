#!/usr/bin/env python3
"""Serves this folder on http://127.0.0.1:<port>/ and opens the viewer. Pixel access (difference,
color channels) needs an http origin; opening index.html from disk shows the images only."""
import http.server, os, socket, sys, threading, webbrowser
os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
while True:
    try: srv = http.server.ThreadingHTTPServer(('127.0.0.1', port), http.server.SimpleHTTPRequestHandler); break
    except OSError: port += 1
url = 'http://127.0.0.1:%d/' % port
print(url); threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try: srv.serve_forever()
except KeyboardInterrupt: pass
