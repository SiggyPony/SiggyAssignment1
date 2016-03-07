

class controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program SDPP \n'
        self.prompt = 'Enter your command: \n'
        self.data = Data()

    def start_game(self):
        self.game.display_game_status()

    def do_move(self, direction):
        print('move', direction)
        result = self.game.move(direction.capitalize())
        if (not result):
            print('You can’t move in that direction or when there are' +
                  ' zombies in the room.')
        else:
            print('You move ' + direction + '.')
            self.game.display_game_status()

    def do_run(self, direction):
        print('run ', direction)
        result = self.game.run(direction.capitalize())
        if (not result):
            print('You can’t run in that direction or when there are no' +
                  ' zombies in the room.')
        else:
            print('You run ' + direction + '.')
            self.game.display_game_status()

    def do_attack(self, line):
        print('attack')
        result = self.game.attack()
        if (not result):
            print('You can\'t attack when there are no zombies.')
        else:
            print('You survived the zombie attack!!')
            self.game.display_game_status()

    def do_cower(self, line):
        print('cower')
        result = self.game.cower()
        if (not result):
            print('You can\'t cower when there is zombies in the room.')
        else:
            print('You cower and regain +3 health.')
            self.game.display_game_status()

    def do_get_item(self, line):
        print('get_item')
        result = self.game.get_item()
        if (not result):
            print('There is no item in the current room.')
        else:
            print('You picked up the item')
            self.game.display_game_status()

    def do_get_totem(self, line):
        print('get totem')
        result = self.game.get_totem()
        if (not result):
            print('You can\'t retrieve the Zombie totem unless you are' +
                  ' in the Evil Temple and there are no Zombies.')
        else:
            print('You picked up the Zombie totem.')
            self.game.display_game_status()

    def do_bury_totem(self, line):
        print('bury totem')
        result = self.game.bury_totem()
        if (not result):
            print('You can only bury the totem in the Graveyard when ' +
                  ' there are no Zombies.')
        else:
            print('You win. The veil of darkness has ' +
                  'lifted, the smell of death leaves!!')
            sys.exit()

    def help_run(self):
        print('run <Direction> 	- Escape zombies by running <Direction>' +
              '. <Direction> = North, East, South, West')

    def help_attack(self):
        print('attack			    - Attack zombies in current room.')

    def help_cower(self):
        print('cower		  	    - Hide in current room and not ' +
              'move this turn.')

    def help_get_item(self):
        print('get_item		    - Retrieve weapon from current room.')

    def help_get_totem(self):
        print('get_totem		    - Retrieve totem (Only' +
              ' in Evil Temple).')

    def help_bury_totem(self):
        print('bury_totem		    - Bury totem (Only in ' +
              'graveyard).')

    def help_save(self):
        print('save <path>		    - Save current game to <path>.')

    def help_load(self):
        print('load <path>		    - ZLoad game from <path>.')

    def help_quit(self):
        print('quit			    - Quit game.')

    def help_move(self):
                print('move <Direction>	- Move player <Direction>. ' +
                      '<Direction> = North, East, South, West')

    def do_save(self, save_string):
        try:
            if (save_string == ''):
                save_string = 'mygame'
            output_file = open(save_string, 'wb')
            pickle.dump(self.game, output_file)
            print('Game saved to ' + save_string)
            output_file.close()
        except Exception as err:
            print(err)
            print('You must enter a file name and/or path to' +
                  ' save too relative to the current directory.')
            print('Eg. ./save/myGameData.dat')

    def do_load(self, load_string):
        try:
            input_file = open(load_string, 'rb')
            self.game = pickle.load(input_file)
            print('Loaded game from ' + load_string)
            self.game.display_game_status()
        except (IOError, pickle.UnpicklingError):
            print('There was an error loading your file ' +
                  load_string + ', please check the path' +
                  ' and file format are correct.')
            return False

    def do_quit(self, line):
        return True