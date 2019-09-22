from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def saluda():
    return render_template("index.html")

@app.route('/<string:page>')
def pages(page):
    return render_template( page )
    
if __name__ == '__main__':
    app.run(debug=True)