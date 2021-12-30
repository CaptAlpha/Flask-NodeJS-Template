import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Arhit Bose Tagore!"

if __name__ == "__main__":
    osPort = os.getenv("PORT")
    if osPort == None:
        port = 5000
    else:
        port = int(osPort)
    app.run(host='0.0.0.0', port=port)
