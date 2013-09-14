from b_classes import *

STATUS_OK = 1;
STATUS_NOT_OK = 0;

class msg_resp:
    status = None
    cause = ''
    def __init__(self, p_status = STATUS_OK, p_cause = ''):
        self.status = p_status
        self.cause = p_cause
#------------------------------------------------------------#
class msg_initEnginReq:
    config_file = None  #config file
    def __init__(self, p_config_file = None):
        self.config_file = p_config_file

class msg_initEnginResp (msg_resp):
    games_list = None    #games served by engine
    def __init__(self, p_status, p_cause, p_games_list = []):
        msg_resp.__init__(self, p_status, p_cause)
        self.games_list = p_games_list
#------------------------------------------------------------#
class msg_initGameReq:
    game_name = None    #name of game
    def __init__ (self, p_game_name):
        self.game_name = p_game_name

class msg_initGameResp (msg_resp):
    armies_list = None   #list of armies avaiable in game
    def __init__(self, p_status, p_cause, p_armies_list = []):
        msg_resp.__init__(self, p_status, p_cause)
        self.armies_list = p_armies_list
#------------------------------------------------------------#
class msg_initArmyReq:
    army_name = None    #name of army
    def __init__ (self, p_army_name):
        self.army_name = p_army_name

class msg_initArmyResp (msg_resp):
    units_list = None       #list of units avaiable in army
    resources_map = None    #map of resources avaiable in army
    def __init__(self, p_status, p_cause, p_units_list = [], p_resources_map = {}):
        msg_resp.__init__(self, p_status, p_cause)
        self.units_list = p_units_list
        self.resources_map = p_resources_map
#------------------------------------------------------------#
class msg_initRosterReq:
    roster_name = None  #name of roster
    roster_file = None  #file with roster to load
    def __init__ (self, p_roster_name = '', p_roster_file = None):
        if(p_roster_file is not None):
            self.roster_file = p_roster_file
        elif(p_roster_name is not None):
            self.roster_name = p_roster_name
        else:
             self.roster_name = ""

class msg_initRosterResp (msg_resp):
    roster = None       #roster object
    def __init__(self, p_status, p_cause, p_roster = None):
        msg_resp.__init__(self, p_status, p_cause)
        self.roster = p_roster
#------------------------------------------------------------#
class msg_createUnitReq:
    unit = None         #init form units list
    unit_name = None    #custom unit name
    def __init__ (self, p_unit, p_unit_name = ''):
        self.unit = p_unit
        self.unit_name = p_unit_name

class msg_createUnitResp (msg_resp):
    pass
#------------------------------------------------------------#
