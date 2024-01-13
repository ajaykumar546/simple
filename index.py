from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def welcom():
    return "Welcome to Flask"

if __name__ == '__main__':
    app.run(debug=True)
