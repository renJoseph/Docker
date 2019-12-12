import SimpleHTTPServer
import SocketServer

PORT = 9000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.server_forever()
