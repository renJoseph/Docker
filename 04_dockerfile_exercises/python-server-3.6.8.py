import http.server
import socketserver

PORT = 9000
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPSever(("", PORT), Handler)
print ("serving at port, PORT")
httpd.serve_forever()
