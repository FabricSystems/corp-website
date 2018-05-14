from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health_route():
    return '{"status": "ok"}'

@app.route('/')
def root_route():
    return '<html><body><h1>hello</h1></body></html>'

if __name__ == '__main__':
    app.run(port=8888)
