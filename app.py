import os
from flask import Flask, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = "my super secret key"


@app.route("/")
def index():
    return "<h1>Homepage </h1>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
