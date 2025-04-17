from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = ""
    if request.method == "POST":
        name = request.form.get("name")
        greeting = f"Hello, {name}!" if name else "Hello, stranger! xD"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
