from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route("/success", methods=['POST'])
def success():
    return render_template("success.html")






if __name__ == '__main__':
    app.debug=True
    app.run()
