from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Получается получилось"
app.run(port='8000')
