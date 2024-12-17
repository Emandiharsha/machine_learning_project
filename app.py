from flask import Flask

app= Flask(__name__)

@app.route("/",methods=["Get","post"])
def index():
    return "Starting machine learning Project"


if __name__ == "__main__":
    app.run(debug=True)