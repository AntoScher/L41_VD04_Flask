import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
#def index():    return render_template('index.html')

def index(): # Чтение содержимого файла index_receipt.html
 with open(os.path.join(os.path.dirname(__file__), 'static', 'index_receipt.html'), 'r', encoding='utf-8') as file:
     receipt_content = file.read()
     return render_template('index.html', receipt_content=receipt_content)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
