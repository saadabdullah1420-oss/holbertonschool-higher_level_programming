#!/usr/bin/python3
"""Provide a simple API using Python's HTTP server."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class APIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for the API endpoints."""

    def do_GET(self):
        """Return text or JSON according to the requested path."""
        if self.path == "/":
            self.send_content(
                200, "Hello, this is a simple API!", "text/plain"
            )
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_content(200, json.dumps(data), "application/json")
        elif self.path == "/status":
            self.send_content(200, "OK", "text/plain")
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_content(200, json.dumps(info), "application/json")
        else:
            self.send_content(404, "Endpoint not found", "text/plain")

    def send_content(self, status, content, content_type):
        """Send a response with its status, headers, and body."""
        body = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("", 8000), APIHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
