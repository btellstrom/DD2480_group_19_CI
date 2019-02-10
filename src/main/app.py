from flask import Flask, request ,render_template
import sys
sys.path.append('./')
from src.main.history import History
from os.path import abspath
from src.main import config

""" Flask application """
app = Flask(__name__)

""" Database of builds """
history = None

@app.route("/", methods = ['GET','POST'])
def hello():
    """
    Receives a payload from a webhook, parses it and send back the result.
    """

    data = request.get_json()# Load JSON data sent with POST request
    return render_template('index.html', data=data)

@app.route("/<build_id>")
def commit_details(build_id):
    """
    Informations on a build can be accessed using the commit ID in the URL.
    
    + build_id - A unique identifier for the build
    """    
    build = history.fetch(build_id)
    return render_template('build.html', build=build)
    
@app.route("/builds")
def build_list():
    """
    Lists the last 10 builds, with a link to the detailed page of a build.
    """
    build_list = history.fetch_n_last(10)
    return render_template('build_list.html', build_list=build_list)

def main():
    """
    Configures the API token and the build database.
    """
    global history
    config.init()
    history = History(config.mongo_database_name, config.mongo_ip, config.mongo_port, config.mongo_user, config.mongo_pass)

if __name__ == '__main__':
    app.run(debug = True, port=8080)
    main()
