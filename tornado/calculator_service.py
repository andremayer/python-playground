import tornado.web

class CalculatorHandler(tornado.web.RequestHandler):
    def get(self, operation):
        try:
            a = float(self.get_argument("a"))
            b = float(self.get_argument("b"))
            
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    self.set_status(400)
                    self.write({"error": "Division by zero"})
                    return
                result = a / b
            else:
                self.set_status(404)
                self.write({"error": "Operation not found"})
                return
                
            self.set_header("Content-Type", "application/json")
            self.write({"a": a, "b": b, "operation": operation, "result": result})
        except ValueError:
            self.set_status(400)
            self.write({"error": "Invalid number format"})
        except tornado.web.MissingArgumentError as e:
            self.set_status(400)
            self.write({"error": f"Missing parameter: {e.arg_name}"})