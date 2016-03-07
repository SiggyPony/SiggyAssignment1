import cmd

from Data import Data

class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program - SDPP \n'
        self.prompt = 'Enter your command: \n'
        self.data = Data()

    def do_load_data(self, line):
        print('load_data')

    def do_save_project(self, line):
        print('save_project')

    def do_load_project(self, line):
        print('load_project')

    def do_show(self, line):
        print('show')

    def do_exit(self, line):
        return True


def main():
    print('Starting')
    controllerTemp = Controller()
    controllerTemp.cmdloop()

if __name__ == '__main__':
    main()