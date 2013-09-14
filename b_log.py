import logging

def init():
    logging.basicConfig(filename='builder_logs.log',filemode='w', format='%(levelname)-8s %(filename)-20s:%(lineno)-4s :   %(message)s', level=logging.INFO)

def init_ut():
    logging.basicConfig(filename='builder_logs.log',filemode='w', format='%(levelname)-8s %(filename)-20s:%(lineno)-4s :   %(message)s', level=logging.DEBUG)    

