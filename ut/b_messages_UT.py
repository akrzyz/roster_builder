#UT for b_messages
import sys
sys.path.append('../')
from b_messages import *
import traceback
import b_log
import logging as LOG

################################################
# Testcases
################################################

def test_msg_initEnginReq():
    msg = msg_initEnginReq("dupa.txt")
    assert msg.config_file == "dupa.txt"
    LOG.info('test_msg_initEnginReq ok')

def test_msg_initEnginResp():
    msg = msg_initEnginResp(STATUS_OK, "", ["qqq","www"])
    assert msg.status == STATUS_OK
    assert msg.cause == ""
    assert msg.games_list == ["qqq","www"]

    msg = msg_initEnginResp(STATUS_NOT_OK, "fucked up")
    assert msg.status == STATUS_NOT_OK
    assert msg.cause == "fucked up"
    assert msg.games_list == []
    LOG.info('test_msg_initEnginResp ok')

def test_msg_initGameReq():
    msg = msg_initGameReq("dupa")
    assert msg.game_name == "dupa"
    LOG.info('test_msg_initGameReq ok')

def test_msg_initGameResp():
    msg = msg_initGameResp(STATUS_OK, "", ["qqq","www"])
    assert msg.status == STATUS_OK
    assert msg.cause == ""
    assert msg.armies_list == ["qqq","www"]

    msg = msg_initGameResp(STATUS_NOT_OK, "fucked up")
    assert msg.status == STATUS_NOT_OK
    assert msg.cause == "fucked up"
    assert msg.armies_list == []
    LOG.info('test_msg_initGameResp ok')

def test_msg_initArmyReq():
    msg = msg_initArmyReq("dupa")
    assert msg.army_name == "dupa"
    LOG.info('test_msg_initArmyReq ok')

def test_msg_initArmyResp():
    msg = msg_initArmyResp(STATUS_OK, "", ["qqq","www"], {"q":"w","e":"r"})
    assert msg.status == STATUS_OK
    assert msg.cause == ""
    assert msg.units_list == ["qqq","www"]
    assert msg.resources_map == {"q":"w","e":"r"}

    msg = msg_initArmyResp(STATUS_NOT_OK, "fucked up")
    assert msg.status == STATUS_NOT_OK
    assert msg.cause == "fucked up"
    assert msg.units_list == []
    assert msg.resources_map == {}
    LOG.info('test_msg_initArmyResp ok')

def test_msg_initRosterReq():
    msg = msg_initRosterReq("dupa")
    assert msg.roster_name == "dupa"
    assert msg.roster_file == None

    msg = msg_initRosterReq(None, "upaupa")
    assert msg.roster_name == None
    assert msg.roster_file == "upaupa"

    msg = msg_initRosterReq("qwe", "rty")
    assert msg.roster_name == None
    assert msg.roster_file == "rty"

    msg = msg_initRosterReq(None, None)
    assert msg.roster_name == ""
    assert msg.roster_file == None
    LOG.info('test_msg_initRosterReq ok')

def test_msg_initRosterResp():
    msg = msg_initRosterResp(STATUS_OK, "", "qqq")
    assert msg.status == STATUS_OK
    assert msg.cause == ""
    assert msg.roster == "qqq"

    msg = msg_initRosterResp(STATUS_NOT_OK, "fucked up")
    assert msg.status == STATUS_NOT_OK
    assert msg.cause == "fucked up"
    assert msg.roster == None
    LOG.info('test_msg_initRosterResp ok')
###########################################
#   run testcases
###########################################
def run_tests():
    try:
        LOG.info('#b_messages_UT start#')
        test_msg_initEnginReq()
        test_msg_initEnginResp()
        test_msg_initGameResp()
        test_msg_initGameResp()
        test_msg_initArmyReq()
        test_msg_initArmyResp()
        test_msg_initRosterReq()
        test_msg_initRosterResp()
        LOG.info('#b_messages_UT done#')
    except:
        traceback.print_exc()
 #       sys.exit(1)

if __name__ == '__main__' :
    b_log.init()
    run_tests()
    print("OK!")
    input()


