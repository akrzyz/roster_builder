#b_xmlreader_UT
import sys
sys.path.append('../')
from b_classes import *
from b_xmlreader import *
import xml.etree.ElementTree as ET
import traceback
import b_log
import logging as LOG
################################################
# Testcases
################################################

def test_read_item():
    i_ref = b_item("bolter","10")    
    i_str = b'<item><name>bolter</name><value>10</value></item>'    
    node = ET.fromstring(i_str)
    assert i_ref == read_item(node)   
    assert i_ref == f_read(node)
    LOG.info('test_read_item ok')
    
def test_read_resource():    
    r_ref = b_resource("knife","ciach, ciach","S + 1")
    r_str = b'<resource><spec>S + 1</spec><name>knife</name><desc>ciach, ciach</desc></resource>'
    node = ET.fromstring(r_str)    
    assert r_ref == read_resource(node) 
    assert r_ref == f_read(node)
    
    r_ref = b_resource("knife","ciach, ciach")
    r_str = b'<resource><spec /><name>knife</name><desc>ciach, ciach</desc></resource>'
    node = ET.fromstring(r_str)    
    assert r_ref == read_resource(node)
    
    r_ref = b_resource("knife")
    r_str = b'<resource><spec /><name>knife</name><desc /></resource>'
    node = ET.fromstring(r_str)    
    assert r_ref == read_resource(node)
    LOG.info('test_read_resource ok')
    
def test_read_property():    
    p_ref = b_property("game_type","w40k",11)
    p_str = b'<property options="11"><name>game_type</name><value>w40k</value></property>'
    node = ET.fromstring(p_str)
    assert p_ref == read_property(node)     
    assert p_ref == f_read(node)
    
    p_ref = b_property("game_type","w40k")
    p_str = b'<property options="7"><name>game_type</name><value>w40k</value></property>'
    node = ET.fromstring(p_str)
    assert p_ref == read_property(node)

    p_ref = b_property("game_type")
    p_str = b'<property options="7"><name>game_type</name><value /></property>'
    node = ET.fromstring(p_str)
    assert p_ref == read_property(node)  
    LOG.info('test_read_property ok')
    
def test_read_stats():        
    s_ref = b_stats();
    s_str = b'<stats />'
    node = ET.fromstring(s_str)
    assert s_ref == read_stats(node) 
    assert s_ref == f_read(node) 
    
    s_ref["S"] = "4"
    s_ref["int"] = "64"
    s_str = b'<stats>int=64,S=4</stats>'
    node = ET.fromstring(s_str)
    assert s_ref == read_stats(node)
    LOG.info("test_read_stats ok")        

def test_read_count():
    c_ref = b_count(1,1,10,3);
    c_str = b'<count><count>1</count><max>10</max><step>3</step><min>1</min></count>'
    node = ET.fromstring(c_str)    
    assert c_ref == read_count(node)
    assert c_ref == f_read(node) 
    LOG.info('test_read_count ok')    
    
def test_read_list():       
    l_ref = b_list('items')
    l_str = b'<list name="items" options="7" />'
    node = ET.fromstring(l_str)
    assert l_ref == read_list(node)
    assert l_ref == f_read(node)
    
    l_ref.append(b_item("aaa","10"))
    l_ref.append(b_item('bbb','22'))
    l_str = b'<list name="items" options="7">\
<item><name>aaa</name><value>10</value></item>\
<item><name>bbb</name><value>22</value></item>\
</list>'
    node = ET.fromstring(l_str)
    assert l_ref == read_list(node)    
    LOG.info('test_read_list ok')    
    
def test_read_map():
    m_ref = b_map('resource_map')
    m_str = b'<map name="resource_map" />'
    node = ET.fromstring(m_str)    
    assert m_ref == read_map(node)
    assert m_ref == f_read(node)
    
    m_ref['skills']
    m_str = b'<map name="resource_map">\
<list name="skills" options="7" />\
</map>'
    node = ET.fromstring(m_str)  
    assert m_ref == read_map(node) 
    
    m_ref['skills'].append(b_item("aaa","10"))
    m_str = b'<map name="resource_map">\
<list name="skills" options="7">\
<item><name>aaa</name><value>10</value></item>\
</list>\
</map>'
    node = ET.fromstring(m_str)
    assert m_ref == read_map(node) 
    LOG.info("test_read_map ok")        
    
def test_read_unit():
    u_ref = b_unit()
    u_str = b'<unit>\
<stats />\
<count><count>1</count><max>1</max><step>1</step><min>1</min></count>\
<list name="properties" options="7">\
<property options="7"><name>name</name><value /></property>\
<property options="7"><name>type</name><value /></property>\
<property options="7"><name>basic_cost</name><value>0</value></property>\
<property options="7"><name>inc_cost</name><value>0</value></property>\
</list>\
<map name="resources" />\
</unit>'
    node = ET.fromstring(u_str)   
    assert u_ref == read_unit(node)
    assert u_ref == f_read(node)

    u_ref.stats.update({"S":"4","int":"64"})
    u_ref.properties.append(b_property('game','w40k'))
    u_ref.resources['weapon'].append(b_item("aaa","10"))
    u_ref.resources['skills'].append(b_item("aaa","10"))
    u_str = b'<unit>\
<count><count>1</count><max>1</max><step>1</step><min>1</min></count>\
<stats>int=64,S=4</stats>\
<list name="properties" options="7">\
<property options="7"><name>name</name><value /></property>\
<property options="7"><name>type</name><value /></property>\
<property options="7"><name>basic_cost</name><value>0</value></property>\
<property options="7"><name>inc_cost</name><value>0</value></property>\
<property options="7"><name>game</name><value>w40k</value></property>\
</list>\
<map name="resources">\
<list name="skills" options="7">\
<item><name>aaa</name><value>10</value></item>\
</list>\
<list name="weapon" options="7">\
<item><name>aaa</name><value>10</value></item>\
</list>\
</map>\
</unit>'
    node = ET.fromstring(u_str)    
    assert u_ref == read_unit(node) 
    LOG.info('test_read_unit ok')    

def test_read_roster():
    r_ref = b_roster()
    r_str = b'<roster>\
<list name="units" options="7" />\
<list name="properties" options="7">\
<property options="7"><name>game_name</name><value /></property>\
<property options="7"><name>army_name</name><value /></property>\
</list>\
<map name="resources" />\
</roster>'
    node = ET.fromstring(r_str)    
    assert r_ref == read_roster(node)
    assert r_ref == f_read(node) 
    LOG.info('test_read_roster ok')
    
###########################################
#   run testcases
###########################################    
def run_tests(): 
    try:
        LOG.info('#b_xmlreader_UT start#')
        test_read_item()
        test_read_resource()
        test_read_property()
        test_read_stats()
        test_read_count()
        test_read_list()
        test_read_map()
        test_read_unit()
        test_read_roster()        
        LOG.info('#b_xmlreader_UT done#')
    except:
        traceback.print_exc()
#        sys.exit(1)

if __name__ == '__main__' :
    b_log.init()
    run_tests()    
    print("OK!")
    input()