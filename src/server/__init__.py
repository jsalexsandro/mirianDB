from flask import Flask,request
from flask_cors import CORS
import configparser
import os
import json
import sys
import colorama

from src.less.Database import Database

def MirianDbServer():
  try:
    ini = open(os.path.join(os.getcwd(),".mirian/props"),"rt",encoding="utf-8").read()
    colorama.init()
  except:
    print("Root not configured!\nRun for Register root:\n $ mirian -r")
    sys.exit()
  
  root = configparser.ConfigParser()
  root.read_string(ini)
  passName = str(int(root["root"]["password"]))
  rootName = root["root"]["default"]
  app = Flask(__name__)
  CORS(app)
  @app.route("/") 
  def index():
    return ""

  @app.route("/@"+rootName,methods=["GET"])
  def func1():
    return "" 

  @app.route(f"/@{rootName}/read-database",methods=["GET"])
  def func2():
    try:
      return json.dumps({"error":False,"values":Database.read(passName)})
    except:
      return json.dumps({"error":True})

  @app.route(f"/@{rootName}/write-database/",methods=["GET"])
  def func3():
    write = request.args.get("value",default = "[]")
    print(write)
    try:
      Database.write(write,passName)
    except:
      return json.dumps({"writed":False})
    return json.dumps({"writed":True})

  print(f"Server Started: http://localhost:7021/@{rootName}")
  app.run(host="localhost",port=7021)