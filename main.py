from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")

def hello_world():
    return render_template() # Внутри () пишем название html-файла в кавычках


if __name__ == "__main__":
    app.run()
"""@app.route("/<name>/")
def hello_world(name="незнакомец"):
    return f"Hello, {name}"
@app.route("/newpage/")
@app.route("/новаястраница/")
def new():    return "new page"

@app.route("/<password>/")
def hello_world(password=None):
    if password == "1234":
        return f"Доступ разрешён"
    else:
        return f"Доступ запрещён"
"""
