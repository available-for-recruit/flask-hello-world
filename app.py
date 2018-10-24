from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

@app.route("/hi")
def hi():
    return "hi"

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
