# We shouldn't install flask in the terminal, it is already imported
import Jack
from Jack import main
from Jack import makeGraph
from flask import Flask,render_template,request
app = Flask(__name__)
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# length =10
# width = 12
# print(list(main(length,width)))

# endpoints
@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/crops")
def crops():
    return app.send_static_file("crops.html")


@app.route("/documentation")
def docs():
    return app.send_static_file("documentation.html")

@app.route("/aboutus")
def aboutus():
    return app.send_static_file("aboutus.html")




# CURRENT WORKING
@app.route("/infoData", methods=["POST","GET"])
def csdata():
    if request.method=="GET":
        data =  request.values

        start =request.values["start"]
        end = request.values["end"]
        location = request.values["end"]
        length = request.values["length"]
        width =request.values["width"]

        return data







#
#         {
#   "button": "submit",
#   "end": "2020",
#   "location": "washington",
#   "panellength": "10",
#   "start": "2019"
# }





# listen
if __name__ == "__main__":
  app.run(port=8888,debug=True)
  # if you need to make it live debuging add 'debug=True'
  # app.run(port=3000, debug=True)
