import sys
from flask import *

flaskapp = Flask(__name__)


class IncorrectPythonVersion(Exception):
  pass
class InvalidRouteValue(Exception):
  pass

class PythonPlugin:
  def __init__(self, python_version):
    global start
    if python_version != sys.version[:3]:
      raise IncorrectPythonVersion("Using incorrect Python version!")
      start = False
    else:
      start = True
    self.start = start

  def pyroute(self, route_, value_, function_=None):
    if function_ != None or function_ != "":
      @flaskapp.route(route_)
      def create_route(function_):
        try:
          return value_
        except:
          return InvalidRouteValue(f"'{value_}' is not a valid value!")
    else:
      @flaskapp.route(route_)
      def create_route():
        try:
          return value_
        except:
          return InvalidRouteValue(f"'{value_}' is not a valid value!")

  def pyrun(self, host_, port_):
    flaskapp.run(host=host_, port=port_)


app = PythonPlugin("3.8")
app.pyroute('/', "e")
app.pyrun('0.0.0.0', 8080)