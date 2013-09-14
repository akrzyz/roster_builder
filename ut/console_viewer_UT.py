#console_viewer_UT
import sys
sys.path.append('../')
sys.path.append('../console')
from b_classes import *
import console_viewer as cv
import traceback
import b_log
import logging as LOG
from copy import deepcopy
################################################
# Testcases
################################################
def test_view_item():
    item = b_item("bolter",10)
    ref_str = "\t[bolter - 10]"
    cv.display(item)
    assert cv.__f_view(item,"\t") == ref_str    
    LOG.info('test_view_item ok')

def test_view_item_short():
    item = b_item("bolter",10)
    ref_str = "\tbolter"
    cv.display_short(item)
    assert cv.__f_view_short(item,"\t") == ref_str    
    LOG.info('test_view_item_short ok')    
    
def test_view_property():
    property = b_property("prop")
    ref_str = "\t7 [prop - ]"
    cv.display(property)
    assert cv.__f_view(property,"\t") == ref_str
    assert cv.__f_view_short(property,"\t") == ref_str

    property = b_property("prop","umpa umpa")
    ref_str = "\t7 [prop - umpa umpa]"
    cv.display(property)
    assert cv.__f_view(property,"\t") == ref_str
    assert cv.__f_view_short(property,"\t") == ref_str    
    LOG.info('test_view_property ok')    
    
def test_view_resource():
    resource = b_resource("qqq")
    ref_str = "\t[qqq -  - ]"
    cv.display(resource)
    assert cv.__f_view(resource,"\t") == ref_str
    assert cv.__f_view_short(resource,"\t") == ref_str

    resource = b_resource("qqq","umpa umpa")
    ref_str = "\t[qqq - umpa umpa - ]"
    cv.display(resource)
    assert cv.__f_view(resource,"\t") == ref_str
    assert cv.__f_view_short(resource,"\t") == ref_str
    
    resource = b_resource("qqq","umpa umpa","ddd")
    ref_str = "\t[qqq - umpa umpa - ddd]"
    cv.display(resource)
    assert cv.__f_view(resource,"\t") == ref_str 
    assert cv.__f_view_short(resource,"\t") == ref_str
    LOG.info('test_view_resource ok')  

def test_view_count():
    count = b_count(6,1,10,2)
    ref_str = "\t[count: 6 min: 1 max: 10 step: 2]"
    cv.display(count)
    assert cv.__f_view(count,"\t") == ref_str   
    assert cv.__f_view_short(count,"\t") == ref_str    
    LOG.info('test_view_count ok')    
    
def test_view_stats():
    stats = b_stats()
    stats["WS"] = 4
    stats["BS"] = 3
    stats["Sv"] = "5+"
    ref_str = "\t[[WS : 4][Sv : 5+][BS : 3]]"
    cv.display(stats)
    assert cv.__f_view(stats,"\t") == ref_str
    assert cv.__f_view_short(stats,"\t") == ref_str    
    LOG.info('test_view_stats ok')

def test_view_list():
    list = b_list("dupa")
    list.append(b_item("bolter",10))
    list.append(b_item("knife",5))
    ref_str = "dupa:\n0 - [bolter - 10]\n1 - [knife - 5]\n"
    cv.display(list)
    assert cv.__f_view(list) == ref_str    
    LOG.info('test_view_list ok')
    
def test_view_list_short():
    list = b_list("dupa")
    list.append(b_item("bolter",10))
    list.append(b_item("knife",5))
    ref_str = "dupa:\n0 - bolter\n1 - knife\n"
    cv.display_short(list)
    assert cv.__f_view_short(list) == ref_str    
    LOG.info('test_view_list_short ok')    
    
def test_view_map():
    map = b_map("dupa")
    map["weapons"].append(b_item("bolter",10))
    map["skills"].append(b_item("jump",15))
    ref_str = "dupa:{\nweapons:\n0 - [bolter - 10]\nskills:\n0 - [jump - 15]\n}"
    cv.display(map)
    assert cv.__f_view(map) == ref_str    
    LOG.info('test_view_map ok')    
    
def test_view_map_short():
    map = b_map("dupa")
    map["weapons"].append(b_item("bolter",10))
    map["skills"].append(b_item("jump",15))
    ref_str = "dupa:{\n0 - weapons\n1 - skills\n}"
    cv.display_short(map)
    assert cv.__f_view_short(map) == ref_str    
    LOG.info('test_view_map_short ok')      

def test_view_unit(): 
    unit = b_unit()
    unit.properties.getByName("name").value = "dupa"
    unit.properties.getByName("type").value = "uber"
    unit.resources["weapons"].append(b_item("bolter",10))
    unit.resources["skills"].append(b_item("jump",15))
    unit.count = b_count(6,1,10,2)
    unit.stats["WS"] = 4
    unit.stats["BS"] = 3
    unit.stats["Sv"] = "5+" 
    ref_str = "unit:{{\n" + cv.__f_view(unit.properties) + "\n" + cv.__f_view(unit.stats) + "\n\n" + cv.__f_view(unit.count) + "\n\n" + cv.__f_view(unit.resources) + "\n}}"
    cv.display(unit)
    assert cv.__f_view(unit) == ref_str
    LOG.info('test_view_unit ok')
    
def test_view_unit_short(): 
    unit = b_unit()
    unit.properties.getByName("name").value = "dupa"
    unit.properties.getByName("type").value = "uber"
    unit.resources["weapons"].append(b_item("bolter",10))
    unit.resources["skills"].append(b_item("jump",15))
    unit.count = b_count(6,1,10,2)
    unit.stats["WS"] = 4
    unit.stats["BS"] = 3
    unit.stats["Sv"] = "5+" 
    ref_str = "unit:{{\n" + cv.__f_view_short(unit.properties) + "\n" + cv.__f_view_short(unit.stats) + "\n\n" + cv.__f_view_short(unit.count) + "\n\n" + cv.__f_view_short(unit.resources) + "\n}}"
    cv.display_short(unit)
    assert cv.__f_view_short(unit) == ref_str
    LOG.info('test_view_unit_short ok')    
    
def test_view_roster(): 
    unit = b_unit()
    unit.properties.getByName("name").value = "tactical"
    unit.properties.getByName("type").value = "troops"
    unit.resources["weapons"].append(b_item("bolter",10))
    unit.resources["skills"].append(b_item("jump",15))
    unit.count = b_count(6,1,10,2)
    unit.stats["WS"] = 4
    unit.stats["BS"] = 3
    unit.stats["Sv"] = "5+"
    
    roster = b_roster()
    roster.properties.getByName("game_name").value = "w40k"
    roster.properties.getByName("army_name").value = "sm"
    roster.units.append(deepcopy(unit))
    
    unit.properties.getByName("name").value = "terminators"
    unit.properties.getByName("type").value = "elite"
    unit.resources["weapons"].getByName("bolter").name = "storm bolter"
    roster.units.append(deepcopy(unit))
    
    roster.resources["teritory"].append(b_item("base",100))
    roster.resources["teritory"].append(b_item("chamber",500))
    
    ref_str = "roster:{{{\n" + cv.__f_view(roster.properties) + "\n" + cv.__f_view(roster.units) + "\n" + cv.__f_view(roster.resources) + "\n}}}"
    cv.display(roster)
    assert cv.__f_view(roster) == ref_str
    
    ref_str_short = "roster:{{{\n" + cv.__f_view_short(roster.properties) + "\n" + cv.__f_view_short(roster.units) + "\n" + cv.__f_view_short(roster.resources) + "\n}}}"
    cv.display_short(roster)
    assert cv.__f_view_short(roster) == ref_str_short
    LOG.info('test_view_roster ok')     
###########################################
#   run testcases
###########################################    
def run_tests(): 
    try:
        LOG.info('#console_viewer_UT start#')
        test_view_item()
        test_view_item_short()
        test_view_property()
        test_view_resource()
        test_view_count()
        test_view_stats()
        test_view_list()
        test_view_list_short()
        test_view_map()
        test_view_map_short()
        test_view_unit()
        test_view_unit_short()
        test_view_roster()
        LOG.info('#console_viewer_UT done#')
    except:
        traceback.print_exc()
#        sys.exit(1)

if __name__ == '__main__' :
    b_log.init()
    run_tests()    
    print("OK!")
    input()