#b_xmlwriter_UT
import sys
sys.path.append('../')
from b_classes import *
from b_xmlwriter import *
import xml.etree.ElementTree as ET
import traceback
import b_log
import logging as LOG
################################################
# Testcases
################################################

def test_write_item():
    i = b_item("bolter","10")
    i_w = write_item(i)
    assert ET.tostring(i_w) == b'<item><name>bolter</name><value>10</value></item>'
    assert ET.tostring(f_write(i)) == b'<item><name>bolter</name><value>10</value></item>'

def test_write_resource():    
    r = b_resource("knife","ciach, ciach","S + 1")
    r_w = write_resource(r)
    assert ET.tostring(r_w) == b'<resource><name>knife</name><desc>ciach, ciach</desc><spec>S + 1</spec></resource>'

def test_write_property():    
    p = b_property("game_type","w40k",11)
    p_w = write_property(p)
    assert ET.tostring(p_w) == b'<property options="11"><name>game_type</name><value>w40k</value></property>'
    LOG.info('test_write_item ok')


def test_write_list():
    l = b_list('items')
    l_w = write_list(l)
    assert ET.tostring(l_w) == b'<list name="items" options="7" />'
    assert ET.tostring(f_write(l)) == b'<list name="items" options="7" />'

    l.append(b_item("aaa","10"))
    l.append(b_item('bbb','22'))
    l_w = write_list(l)
    assert ET.tostring(l_w) == b'<list name="items" options="7">\
<item><name>aaa</name><value>10</value></item>\
<item><name>bbb</name><value>22</value></item>\
</list>'
    LOG.info('test_write_list ok')

def test_write_map():
    m = b_map('resource_map')
    m_w = write_map(m)
    assert ET.tostring(m_w) == b'<map name="resource_map" />'
    assert ET.tostring(f_write(m)) == b'<map name="resource_map" />'

    m['skills']
    m_w = write_map(m)
    assert ET.tostring(m_w) == b'<map name="resource_map">\
<list name="skills" options="7" />\
</map>'

    m['skills'].append(b_item("aaa","10"))
    m_w = write_map(m)
    assert ET.tostring(m_w) == b'<map name="resource_map">\
<list name="skills" options="7">\
<item><name>aaa</name><value>10</value></item>\
</list>\
</map>'
    LOG.info("test_write_map ok")
    
def test_write_stats():
    s = b_stats();
    s_w = write_stats(s)
    assert ET.tostring(s_w) == b'<stats />'
    assert ET.tostring(f_write(s)) == b'<stats />'

    s["S"] = "4"
    s["int"] = "64"
    s_w = write_stats(s)
    assert ET.tostring(s_w) == b'<stats>int=64,S=4</stats>'
    LOG.info("test_write_stats ok")
    
def test_write_count():
    c = b_count(1,1,10,3);
    c_w = write_count(c)
    assert ET.tostring(c_w) == b'<count><count>1</count><min>1</min><max>10</max><step>3</step></count>'
    assert ET.tostring(f_write(c)) == b'<count><count>1</count><min>1</min><max>10</max><step>3</step></count>'
    LOG.info("test_write_stats ok")    

def test_write_unit():
    u = b_unit()
    u_w = write_unit(u)
    assert ET.tostring(u_w) == b'<unit>\
<list name="properties" options="7">\
<property options="7"><name>name</name><value /></property>\
<property options="7"><name>type</name><value /></property>\
<property options="7"><name>basic_cost</name><value>0</value></property>\
<property options="7"><name>inc_cost</name><value>0</value></property>\
</list>\
<stats />\
<count><count>1</count><min>1</min><max>1</max><step>1</step></count>\
<map name="resources" />\
</unit>'
    assert ET.tostring(u_w) == ET.tostring(f_write(u))

    u.stats.update({"S":"4","int":"64"})
    u.properties.append(b_property('game','w40k'))
    u.resources['weapon'].append(b_item("aaa","10"))
    u.resources['skills'].append(b_item("aaa","10"))
    u_w = write_unit(u)
    assert ET.tostring(u_w) == b'<unit>\
<list name="properties" options="7">\
<property options="7"><name>name</name><value /></property>\
<property options="7"><name>type</name><value /></property>\
<property options="7"><name>basic_cost</name><value>0</value></property>\
<property options="7"><name>inc_cost</name><value>0</value></property>\
<property options="7"><name>game</name><value>w40k</value></property>\
</list>\
<stats>int=64,S=4</stats>\
<count><count>1</count><min>1</min><max>1</max><step>1</step></count>\
<map name="resources">\
<list name="skills" options="7">\
<item><name>aaa</name><value>10</value></item>\
</list>\
<list name="weapon" options="7">\
<item><name>aaa</name><value>10</value></item>\
</list>\
</map>\
</unit>'
    LOG.info('test_write_unit ok')

def test_write_roster():
    r = b_roster()
    r_w = write_roster(r)
    assert ET.tostring(r_w) == b'<roster>\
<list name="properties" options="7">\
<property options="7"><name>game_name</name><value /></property>\
<property options="7"><name>army_name</name><value /></property>\
</list>\
<list name="units" options="7" />\
<map name="resources" />\
</roster>'
    assert ET.tostring(r_w) == ET.tostring(f_write(r))
    LOG.info('test_write_roster ok')

def test_f_write():
    i = b_item("bolter","10")
    i_w = f_write(i)
    assert ET.tostring(i_w) == b'<item><name>bolter</name><value>10</value></item>'

    l_str = 'dsadsa';
    oops = f_write(l_str)
    assert oops is None
    l_int = 12
    oops = f_write(l_int)
    assert oops is None
    LOG.info('test_f_write ok')


###########################################
#   run testcases
###########################################
def run_tests():
    try:
        LOG.info('#b_xmlwriter_UT start#')
        test_write_item()
        test_write_resource()
        test_write_property()
        test_write_list()
        test_write_map()
        test_write_stats()
        test_write_count()
        test_write_unit()
        test_write_roster()
        test_f_write()
        LOG.info('#b_xmlwriter_UT done#')
    except:
        traceback.print_exc()
#        sys.exit(1)

if __name__ == '__main__' :
    b_log.init()
    run_tests()
    print("OK!")
    input()