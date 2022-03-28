from src.server import MirianDbServer
from src.less.Reg import Register
import sys

CLI_HELP_MESSAGE = """MirianDB version: [version]
usage:
  $ mirian <arguments>
  --help, -h for help with cli
  --verison, -f for get verison of MirianDB
  --register, -r for register api of database
"""

class MirianCli:
  argv = sys.argv
  CLI_VERSION = "0.1"

  def __init__(self): 
    self.addCommand([],self._default)
    self.addCommand(["-h","--help"],self._help)
    self.addCommand(["-v","--version"],self._version)
    self.addCommand(["-r","--register"],Register)

  def _default(self,props):
    MirianDbServer()

  def _help(self,props):
    print(
      CLI_HELP_MESSAGE.
      replace("[version]",self.CLI_VERSION)  
    )

  def _version(self,props):
    print(f"MirianDB version: {self.CLI_VERSION}")

  def addCommand(self,command:list,calback):
    localDetected = None
    detectedCommand = False

    if command == []:
      if len(self.argv) == 1:
        calback([])

    for count,a in enumerate(self.argv):
      for c in command:
        if c == a:
          detectedCommand = True
          localDetected = count
          break

      if (detectedCommand == True):
        calback(
          self.argv[localDetected+1:]
        )
        break
