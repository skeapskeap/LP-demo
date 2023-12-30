import os

from flask import Flask

app = Flask(__name__)
some_env = os.getenv('ENV_VAR')


@app.route("/")
def hello_world():
    return f"<p>Hello, World! {some_env=}</p>"
