#!flask/bin/python
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/sendata', methods=['POST'])
def post():
    content = request.get_json()
    
    return "data posted"

if __name__ == '__main__':
    app.run(debug=True)
