import logging as LOG

class state:
    """ dispatch_table - table maping msg type to msg handler """
    dispatch_table = {}
    def __init__(self):
        pass

    """ handle(msg) - call registred msg handler or handleUnexpected if no handler is registred """
    def handle(self, p_msg):
        handler = self.dispatch_table.get(type(p_msg))
        if(handler):
            return handler(p_msg)
        else:
            LOG.error("Unexpected Msg: " + str(type(p_msg)) + " in state" + str(type(self)))
            return handleUnexpected(p_msg)

    """ register(msg_type, handler) - register handler for given msg type """
    def register(self, p_msg_type, p_handler):
        self.dispatch_table[p_msg_type] = p_handler

    """ handleUnexpected(p_msg) - handler for unexpected msg """
    def handleUnexpected(self, p_msg):
        return false
