from flask import Flask,request
import configparser
import os
import json
import sys

from src.less.Database import Database

def MirianDbServer():
  try:
    ini = open(os.path.join(os.getcwd(),".mirian/props"),"rt",encoding="utf-8").read()
  except:
    print("Root not configured!\nRun for Register root:\n $ mirian -r")
    sys.exit()
  
  root = configparser.ConfigParser()
  root.read_string(ini)
  passName = str(int(root["root"]["password"]))
  rootName = root["root"]["default"]
  app = Flask(__name__)

  @app.route("/") 
  def index():
    return ""

  @app.route("/@"+rootName)
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

  app.run(host="0.0.0.0",port=7021)