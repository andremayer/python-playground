import tornado.web
import json
import hashlib

class TextStatsHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            text = data.get("text", "")
            
            stats = {
                "character_count": len(text),
                "word_count": len(text.split()),
                "line_count": len(text.splitlines()),
                "uppercase_count": sum(1 for c in text if c.isupper()),
                "lowercase_count": sum(1 for c in text if c.islower()),
                "digit_count": sum(1 for c in text if c.isdigit())
            }
            
            self.set_header("Content-Type", "application/json")
            self.write(stats)
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON"})

class HashHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            text = data.get("text", "")
            
            hashes = {
                "md5": hashlib.md5(text.encode()).hexdigest(),
                "sha1": hashlib.sha1(text.encode()).hexdigest(),
                "sha256": hashlib.sha256(text.encode()).hexdigest()
            }
            
            self.set_header("Content-Type", "application/json")
            self.write(hashes)
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON"})

class ReverseHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            text = data.get("text", "")
            
            result = {
                "original": text,
                "reversed": text[::-1],
                "words_reversed": " ".join(text.split()[::-1])
            }
            
            self.set_header("Content-Type", "application/json")
            self.write(result)
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON"})