from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():

    return render_template('poses.html')

@app.route('/post', methods=['POST'])
def process():
    data = request.get_json()
    print(data)

    return data

@app.route('/home.html')
def home():

    return render_template('home.html')