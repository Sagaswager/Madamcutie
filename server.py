import http.server
import socketserver
import urllib.parse
import json
import os
import base64

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_POST(self):
        # Support /save_html (legacy and inline editor fallback)
        if self.path == '/save_html':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                filename = data.get('file') or data.get('filePath')
                content = data.get('content')
                
                # Check for permitted files
                allowed_files = ['shop.html', 'index.html', 'about.html', 'contact.html', 'policy.html', 'product.html', 'creators.html']
                if filename in allowed_files:
                    file_path = os.path.join(os.getcwd(), filename)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'{"status":"success","success":true}')
                else:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'{"status":"invalid file","success":false,"error":"invalid file"}')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"status":"error", "success": False, "message": str(e), "error": str(e)}).encode('utf-8'))
            return

        # Support /api/save-content (used by admin.html)
        elif self.path == '/api/save-content':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                file_path_rel = data.get('filePath')
                content = data.get('content')
                
                if not file_path_rel or content is None:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'{"success": false, "error": "Missing filePath or content"}')
                    return
                
                # Normalize and prevent directory traversal
                normalized_path = os.path.normpath(file_path_rel)
                if normalized_path.startswith('..') or os.path.isabs(normalized_path):
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'{"success": false, "error": "Invalid file path"}')
                    return
                
                full_path = os.path.join(os.getcwd(), normalized_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"success": true}')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
            return

        # Support /api/upload-image (used by admin.html)
        elif self.path == '/api/upload-image':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                file_name = data.get('fileName')
                file_content_base64 = data.get('fileContent')
                
                if not file_name or not file_content_base64:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'{"success": false, "error": "Missing fileName or fileContent"}')
                    return
                
                # Decode base64
                file_data = base64.b64decode(file_content_base64)
                
                # Check file_name to prevent directory traversal
                normalized_name = os.path.normpath(file_name)
                if normalized_name.startswith('..') or os.path.isabs(normalized_name):
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b'{"success": false, "error": "Invalid file name"}')
                    return
                
                file_path = os.path.join(os.getcwd(), 'assets', 'images', 'madam', normalized_name)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'wb') as f:
                    f.write(file_data)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "path": f"/assets/images/madam/{normalized_name}"}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
            return
            
        self.send_error(404, "File not found")

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"Admin Server running on port {PORT}...")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}. Port {PORT} is probably in use. Please kill the existing server first.")
