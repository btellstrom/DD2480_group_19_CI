from flask import Flask, request ,render_template
app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def hello():

    data = request.get_json(silent=True)# Load JSON data sent with POST request
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug = True, port=8080)