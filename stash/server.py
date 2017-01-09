#!/usr/bin/python
    
import SimpleHTTPServer
import SocketServer
import webbrowser
 
PORT = 8001
    
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});
    
httpd = SocketServer.TCPServer(("", PORT), Handler)
    
print "Serving at port", PORT

webbrowser.open_new('--kiosk http://127.0.0.1:' + str(PORT))

httpd.serve_forever()