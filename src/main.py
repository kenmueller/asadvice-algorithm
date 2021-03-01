from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'asadvice'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
