#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type='text/plain; charset=utf-8'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers(200, 'text/plain; charset=utf-8')
            self.wfile.write(b"Hello, this is a simple API!")
            return

        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            payload = json.dumps(data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(payload)
            return

        if self.path == '/status':
            self._set_headers(200, 'text/plain; charset=utf-8')
            self.wfile.write(b"OK")
            return

        if self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._set_headers(200, 'application/json; charset=utf-8')
            self.wfile.write(json.dumps(info).encode('utf-8'))
            return

        self._set_headers(404, 'text/plain; charset=utf-8')
        self.wfile.write(b"Endpoint not found")

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length > 0 else b''
        try:
            data = json.loads(body.decode('utf-8')) if body else {}
            response = {"received": data}
            self._set_headers(200, 'application/json; charset=utf-8')
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except json.JSONDecodeError:
            self._set_headers(400, 'text/plain; charset=utf-8')
            self.wfile.write(b"Invalid JSON")


def run(host='', port=8000):
    server = HTTPServer((host, port), SimpleHandler)
    print(f"Starting server on http://{host or 'localhost'}:{port}  (Ctrl+C to stop)")
    server.serve_forever()


if __name__ == '__main__':
    run()
