from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"
@app.route("/new/")


@app.route("/newpage/")

@app.route("/новаястраница/")
def new():
    return "new page"



if __name__ == "__main__":
    app.run()

