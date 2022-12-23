from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"hello my name is alhad kabir"

if __name__ == "__main__":
    app.run(debug=True)