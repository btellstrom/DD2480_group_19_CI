from flask import Flask, request ,render_template
from main.history import History
from os.path import abspath
from main import config
app = Flask(__name__)

# Database of builds
history = None

@app.route("/", methods = ['GET','POST'])
def hello():

    data = request.get_json()# Load JSON data sent with POST request
    return render_template('index.html', data=data)


def main():
    global history
    config.init()
    history = History(config.mongo_database_name, config.mongo_ip, config.mongo_port, config.mongo_user, config.mongo_pass)

if __name__ == '__main__':
    app.run(debug = True, port=8080)
    main()
