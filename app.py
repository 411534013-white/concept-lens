"""
ConceptLens Local Server Runner
-------------------------------
輕量級本地 HTTP 伺服器，自動開啟瀏覽器體驗 ConceptLens。
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(f"🚀 ConceptLens 本地伺服器已啟動: {url}")
        print(f"🖥️ 簡報頁面直接訪問: {url}/slides.html")
        print("🛑 按下 Ctrl + C 可終止伺服器")
        print("=" * 60)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n伺服器已安全停止。")
            sys.exit(0)

if __name__ == "__main__":
    main()
