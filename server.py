# We shouldn't install flask in the terminal, it is already imported
from flask import Flask,render_template
app = Flask(__name__)



@app.route("/")
def home():
  return app.send_static_file("index.html")




# listen
if __name__ == "__main__":
  app.run(port=8888,debug=True)
  # if you need to make it live debuging add 'debug=True'
  # app.run(port=3000, debug=True)
