from b_classes import *
from b_xmlreader import *
from b_xmlwriter import *
from b_engine import *
import logging as LOG

class console_xml_editor:
    engine = None;
    def __init_engine(self):
        config_file = input("enter config file, or press enter for default: ")
        if config_file = "" :
            self.engine = b_engine()
        else:
            self.engine = b_engine(config_file)
        if engine.config is None :
            print("Initialization engin with config file: " + str(engine.config_file) + " failed!")
            return False
        else:
            print("engine started!")
            return True
                
    def __select_game(self):
        print("avaiable games:")
        i = 0;
        for game in self.engine.config:
            print(str(i) + " - " + str(game.name))
            i++
        print("a - add new game")
        print("b - back")
        option = input("chose option: ")
        #handler do napisania
        
    def __init_game(self,game_name):
        self.engine.init_game(game_name)
        if self.engine.game_config is None :
            print("Initialization game: " + str(game_name) + " from file: " + str(self.engine.game_config_file) + " failed!")
            return False
        else:
            print("game initialized")
            return True
            
    def __select_army(self):
        print("avaiable armies:")
        i = 0;
        for army in self.engine.game_config:
            print(str(i) + " - " + str(army.name))
            i++
        print("a - add new army")
        print("b - back")
        option = input("chose option: ")
        
    def __init_army(self,army_name):
        self.engine.init_army(game_name)        
        