from flask import Flask

app = Flask(__name__)

@app.route("/cookie")
def give_cookie():
    return "🍪 Here's your cookie!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
