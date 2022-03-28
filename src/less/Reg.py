import os
import random

class Register:
  def __init__(self,props):
    self.run()

  def run(self):
    while True:
      print("Configure root")
      root = input("root name: ").strip()
      if root == "":
        continue
      if " " in root:
        continue

      self.createRoot(root)
      break

  
  def createRoot(self,root):
    if not os.path.exists("./.mirian"):
      os.mkdir("./.mirian")

    with open("./.mirian/props","wt+",encoding="utf-8") as ini:
      ini.write(f"[root]\ndefault = {root}\npassword = {random.randint(99999999,9999999999999909)}")
      print("Registed! ")

    return True
    