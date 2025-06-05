from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route("/media")
def media():
    return render_template('media.html', title='Media')

@app.route("/chat")
def chat():
    return render_template('chat.html', title='Chat')

@app.route("/file")
def file():
    return render_template('file.html', title='File')

if __name__ == '__main__':
    app.run(debug=True)