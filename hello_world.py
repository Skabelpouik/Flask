from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "It is your destiny!"

if __name__ == "__main__" and "get_ipython" not in locals():
    app.run()

