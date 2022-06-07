'''
Dummy data when real ones aren't enough

GG
'''


import os
from flask import Flask, jsonify
import requests
from random import randint


app = Flask(__name__)
app.secret_key = f"{os.urandom(12)}"


@app.route("/data")
def dummy():
    val = [randint(102,121), randint(72,81), randint(94,98), randint(35,39)]
    payload = { "ex":str(val[0]),
                "hx":str(val[1]),
                "sx": str(val[2]),
                "tx": str(val[3])
              }

    return jsonify(payload)





if __name__ == "__main__":
   app.run()
        