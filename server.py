import http.server
import socketserver
import urllib.parse
import json
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save_html':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                filename = data.get('file')
                content = data.get('content')
                
                # Security: only allow saving specific files in the root dir
                if filename in ['shop.html', 'index.html']:
                    file_path = os.path.join(os.getcwd(), filename)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(b'{"status":"success"}')
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b'{"status":"invalid file"}')
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"status":"error", "message": str(e)}).encode('utf-8'))
            return
            
        self.send_error(404, "File not found")

# Stop the existing python -m http.server process if we can, or we can just tell the user to run this script.
# Wait, the user might be running `python -m http.server` manually. 
# I will run this server on port 8000. If it fails, it means the other server is running.
# I will kill the old background process first.

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"Admin Server running on port {PORT}...")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}. Port {PORT} is probably in use. Please kill the existing server first.")
