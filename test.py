from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>HELLO BIKU................</h1>"

@app.route("/a")
def hello_worlda():
    return "<h1>HELLO Bikkkkkuuuuuuuuuuuuu        aa   ................</h1>"


@app.route("/test")
def test():
    a = 4*8
    return "This is test function {}".format(a)

@app.route("/testin")
def test_input():
    data = request.args.get("x")
    return "this is test input  kkkkkk     {}".format(data)


@app.route("/b")
def hello_worldb():
    return "<h1>HELLO ........b........</h1>"

@app.route("/c")
def hello_worldc():
    return "<h1>HELLO Bikash........c........</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
