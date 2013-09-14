from b_classes import *
from b_messages import *
from b_state import *

class engine_controler:
    state = None
    def __init__(self):
        pass

class waitForInitialize (state):
    engine = None
    def __init__(sefl, p_engine):
        self.engine = p_engine
        register(msg_initEnginReq, handle_initEnginReq)

    def __handle_initEnginReq(self, p_msg):
        if(p_msg.config_file):
            self.engine(p_msg.config_file)
        else:
            self.engine();

        if(self.engine.config):
            return __respOK()
        else:
            return __respNotOK()

    def __respOK(self):
        return msg_initEnginResp(STATUS_OK,"",__makeGamesList())

    def __respNotOK(self):
        return msg_initEnginResp(STATUS_NOT_OK, "start engine failed")

    def __makeGamesList(self):
        games_list = []
        for elem in self.engin.config:
            games_list.append(elem.name)
        return games_list
