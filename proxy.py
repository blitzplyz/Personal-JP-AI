#!/usr/bin/env python3
"""
Hayai Proxy - runs on your PC, bridges Ollama to the internet via ngrok
Usage: python proxy.py
Then tunnel port 8080 with ngrok: ngrok http 8080
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json, urllib.request, urllib.error

OLLAMA = "http://localhost:11434"

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[Hayai] {args[0]} {args[1]}")

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        try:
            req = urllib.request.Request(OLLAMA + self.path)
            with urllib.request.urlopen(req) as r:
                body = r.read()
            self.send_response(200)
            self.send_cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        except Exception as e:
            self.send_response(502)
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            req = urllib.request.Request(
                OLLAMA + self.path,
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req) as r:
                resp_body = r.read()
            self.send_response(200)
            self.send_cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(resp_body)
        except Exception as e:
            self.send_response(502)
            self.send_cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Hayai proxy running on http://localhost:8080")
    print("Now run: ngrok http 8080")
    server.serve_forever()
