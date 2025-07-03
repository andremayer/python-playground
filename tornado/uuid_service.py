import tornado.web
import uuid

class UUIDHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write({"uuid": str(uuid.uuid4())})

class UUIDListHandler(tornado.web.RequestHandler):
    def get(self):
        count = int(self.get_argument("count", 1))
        count = min(count, 100)
        uuids = [str(uuid.uuid4()) for _ in range(count)]
        self.set_header("Content-Type", "application/json")
        self.write({"uuids": uuids, "count": len(uuids)})