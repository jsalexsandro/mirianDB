import os,sys
from src.less.Cip import decode, encode

class Database:
  @staticmethod
  def exists():
    if not os.path.exists("./.mirian/parser"):
      os.mkdir("./.mirian/parser")

  @staticmethod
  def write(values,key):
    Database.exists()
    with open("./.mirian/parser/structure","wt+",encoding="utf-8") as fs:
      fs.write(encode(key,values))

  @staticmethod
  def read(key):
    Database.exists()
    with open("./.mirian/parser/structure","rt",encoding="utf-8") as fs:
      return decode(key,fs.read())
  