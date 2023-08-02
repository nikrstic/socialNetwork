import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT),Handler)
print("Otvoreno na portu: " , PORT)
httpd.serve_forever()
