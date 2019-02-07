from flask import Flask, request ,render_template
from main.history import History
from os.path import abspath
from main import config
app = Flask(__name__)

# Database of builds
history = None

@app.route("/", methods = ['GET','POST'])
def hello():

    data = request.get_json(silent=True)# Load JSON data sent with POST request
    return render_template('index.html', data=data)

"""
Informations on a build can be accessed using the commit ID in the URL.

:build_id: A unique identifier for the build
"""    
@app.route("/<build_id>")
def commit_details(build_id):
    build = history.fetch(build_id)
    return render_template('build.html', build=build)
    

def main():
    global history
    config.init()
    history = History(config.mongo_database_name, config.mongo_ip, config.mongo_port, config.mongo_user, config.mongo_pass)

if __name__ == '__main__':
    app.run(debug = True, port=8080)
    main()