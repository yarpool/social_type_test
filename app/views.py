from flask import render_template
from flask import request
from app import app


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("main.html")
    elif request.method == 'POST':
        return "форма отправлена"
