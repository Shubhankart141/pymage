from flask import Flask, render_template, url_for
app = Flask(__name__)

file = open("images.txt","r")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Let the internet surprise you!")


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
