import tornado.web
import random
import math

class RandomHandler(tornado.web.RequestHandler):
    def get(self):
        min_val = int(self.get_argument("min", 1))
        max_val = int(self.get_argument("max", 100))
        count = int(self.get_argument("count", 1))
        count = min(count, 1000)
        
        numbers = [random.randint(min_val, max_val) for _ in range(count)]
        
        self.set_header("Content-Type", "application/json")
        self.write({
            "numbers": numbers,
            "count": len(numbers),
            "min_range": min_val,
            "max_range": max_val
        })

class PrimeHandler(tornado.web.RequestHandler):
    def get(self):
        number = int(self.get_argument("number"))
        
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        self.set_header("Content-Type", "application/json")
        self.write({
            "number": number,
            "is_prime": is_prime(number)
        })

class FactorialHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            number = int(self.get_argument("number"))
            if number < 0:
                self.set_status(400)
                self.write({"error": "Factorial not defined for negative numbers"})
                return
            if number > 20:
                self.set_status(400)
                self.write({"error": "Number too large (max 20)"})
                return
                
            result = math.factorial(number)
            
            self.set_header("Content-Type", "application/json")
            self.write({
                "number": number,
                "factorial": result
            })
        except ValueError:
            self.set_status(400)
            self.write({"error": "Invalid number format"})