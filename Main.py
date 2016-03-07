import cmd
from Data import Data

class Main(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program SDPP \n'
        self.prompt = 'Enter your command: \n'
        self.data = Data()
        