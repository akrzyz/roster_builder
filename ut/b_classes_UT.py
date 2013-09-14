#UT for b_classes
import sys
sys.path.append('../')
from b_classes import *
import traceback
import b_log
import logging as LOG

################################################
# Testcases
################################################

def test_b_name():
    n = b_name('asd')
    assert n.name == 'asd'
    LOG.info('test_b_name ok')
    
def test_b_type_name():
    t = b_type_name('zxc')
    assert t.type_name == 'zxc'
    LOG.info('test_b_type_name ok')

def test_b_options():
    o = b_options()
    assert o.getOpt() == VISABLE | EDITABLE | COUNTABLE
    assert o.getOpt(VISABLE)
    assert o.getOpt(EDITABLE)
    assert o.getOpt(COUNTABLE)
    o.setOpt(8)
    assert o.getOpt(8)
    assert o.getOpt() == 15
    o.clearOpt(1)
    assert o.getOpt(1) == 0
    assert o.getOpt() == 14
    LOG.info("test_b_options ok")

def test_b_list():
    l = b_list('myList');
    assert l.type_name == 'list'
    assert l.name == 'myList'
    assert l.getOpt() == VISABLE | EDITABLE | COUNTABLE
    assert len(l) == 0
    l.append(666);
    l.append(222);
    assert l[0] == 666
    assert l[1] == 222
    assert len(l) == 2
    
    l.setOpt(8)
    assert l.getOpt(8)    
    assert not l.empty()
    LOG.info('test_b_list ok')
    
def test_b_list_empty():
    l = b_list('das')
    assert l.empty()
    l.append(3)
    assert not l.empty()
    l.pop()
    assert l.empty()
    LOG.info('test_b_list_empty ok')
    
def test_b_resource():
    r = b_resource('aaa')
    assert r.type_name == 'resource'
    assert r.name is not None
    assert r.desc is not None   
    assert r.spec is not None
    assert r.name == 'aaa'
    r.desc = 'bla bla'
    assert r.desc == 'bla bla'
    r.spec = 'puf'
    assert r.spec == 'puf'
    
    r2 = b_resource('qqq','www','eee')
    assert r2.name == 'qqq'
    assert r2.desc == 'www'
    assert r2.spec == 'eee'
    LOG.info('test_b_resource ok')
    
def test_b_map():
    m = b_map('rrr')
    assert m.type_name == 'map'
    assert m['yuitu'] is not None
    assert isinstance(m['ghjhghj'], b_list)
    m['a'].append(222)
    m['a'].append(666)
    assert m['a'][0] == 222
    assert m['a'][1] == 666
    LOG.info('test_b_map ok')
    
def test_b_item():
    i = b_item("bolter","100")
    assert i.type_name == 'item'
    assert i.name == 'bolter'
    assert i.value == '100'
    i.name = "asd"
    assert i.name == 'asd'
    i.value = '666'
    assert i.value == '666'
    LOG.info('test_b_item ok')
    
def test_b_property():
    p = b_property("qqq")
    assert p.type_name == 'property'
    assert p.name == 'qqq'
    assert p.value == ''
    assert p.getOpt() == VISABLE | EDITABLE | COUNTABLE
    p.name = "asd"
    assert p.name == 'asd'
    p.value = '666'
    assert p.value == '666'
    p2 = b_property("qqqq",'wwww')
    assert p2.name == 'qqqq'
    assert p2.value == 'wwww'
    assert p2.getOpt() == VISABLE | EDITABLE | COUNTABLE
    
    p3 = b_property("eee",'rrr',9)
    assert p3.name == 'eee'
    assert p3.value == 'rrr'
    assert p3.getOpt() == 9
    LOG.info('test_b_property ok')

def test_b_unit():
    u = b_unit()
    assert u.type_name == 'unit'
    assert u.stats is not None
    assert isinstance(u.stats,dict)
    assert u.resources is not None
    assert isinstance(u.resources,b_map)
    assert u.properties is not None
    assert isinstance(u.properties,b_list)
    assert len(u.properties) == 4
    assert u.properties.getByName('name') is not None
    assert u.properties.getByName('type') is not None
    assert u.properties.getByName('basic_cost') is not None
    assert u.properties.getByName('inc_cost') is not None
    assert u.properties.getByName('basic_cost').value == '0'
    assert u.properties.getByName('inc_cost').value == '0' 
    
    u.properties.getByName('basic_cost').value  = '50'
    u.properties.getByName('inc_cost').value  = '15'
    assert u.properties.getByName('basic_cost').value == '50'
    assert u.properties.getByName('inc_cost').value == '15'
   
    u.stats.setdefault('S','11')
    assert u.stats.get('S') == '11'
    
    u.resources['weapons'].append(b_item("bolter","15"))
    assert u.resources['weapons'].getByName('bolter') is not None
    assert u.resources['weapons'].getByName('bolter').name == 'bolter'
    assert u.resources['weapons'].getByName('bolter').value == '15'
    u.resources['weapons'].append(b_item("las pistol","5"))
    assert u.resources['weapons'].getByName('las pistol') is not None
    assert u.resources['weapons'].getByName('las pistol').name == 'las pistol'
    assert u.resources['weapons'].getByName('las pistol').value == '5'
    
    u.resources['skills'].append(b_item("jump","10"))
    assert u.resources['skills'].getByName('jump') is not None
    assert u.resources['skills'].getByName('jump').name == 'jump'
    assert u.resources['skills'].getByName('jump').value == '10'
    u.resources['skills'].append(b_item("run","0"))
    assert u.resources['skills'].getByName('run') is not None
    assert u.resources['skills'].getByName('run').name == 'run'
    assert u.resources['skills'].getByName('run').value == '0'    
    
    u.count.max = 4
    u.count.increment()
    u.count.increment()
    assert u.count_value() == 110
    assert u.properties.getByName('value').value == '110'
    LOG.info('test_b_unit ok')
    
def test_b_roster():
    r = b_roster()
    assert r.type_name == 'roster'
    assert r.units is not None
    assert isinstance(r.units,list)
    assert r.resources is not None
    assert isinstance(r.resources,b_map)
    assert r.properties is not None
    assert isinstance(r.properties,b_list)
    assert len(r.properties) == 2
    assert r.properties.getByName('game_name') is not None
    assert r.properties.getByName('army_name') is not None
    
    assert len(r.units) == 0
    r.units.append(b_unit())
    assert len(r.units) == 1
    assert isinstance(r.units[0],b_unit)
    
    r.resources['weapons'].append(b_item("bolter","11"))
    assert r.resources['weapons'].getByName('bolter') is not None
    assert r.resources['weapons'].getByName('bolter').name == 'bolter'
    assert r.resources['weapons'].getByName('bolter').value == '11'
    LOG.info('test_b_roster ok')    
    
def test_b_stats():
    s = b_stats()
    assert s.type_name == 'stats'
    s['S'] = "10"
    s['W'] = "2"
    assert s["S"] == "10"
    assert s["W"] == "2"
    LOG.info('test_b_stats ok') 
    
def test_b_count(): 
    c = b_count()
    assert c.min == 1
    assert c.max == 1
    assert c.step == 1
    assert c.count == 1    
    c.increment()
    assert c.min == 1
    assert c.max == 1
    assert c.step == 1
    assert c.count == 1
    c.decrement()
    assert c.min == 1
    assert c.max == 1
    assert c.step == 1
    assert c.count == 1
    
    c2 = b_count(1,1,10,3)
    assert c2.min == 1
    assert c2.max == 10
    assert c2.step == 3
    assert c2.count == 1    
    c2.increment()
    assert c2.min == 1
    assert c2.max == 10
    assert c2.step == 3
    assert c2.count == 4
    c2.decrement()
    assert c2.min == 1
    assert c2.max == 10
    assert c2.step == 3
    assert c2.count == 1
    LOG.info('test_b_count ok') 
    
###########################################
#   run testcases
###########################################    
def run_tests(): 
    try:
        LOG.info('#b_classes_UT start#')
        test_b_name()
        test_b_type_name()
        test_b_options()
        test_b_list() 
        test_b_list_empty()
        test_b_resource()
        test_b_map()
        test_b_item()
        test_b_property()
        test_b_unit()
        test_b_roster()
        test_b_stats()
        test_b_count()
        LOG.info('#b_classes_UT done#')
    except:
        traceback.print_exc()
 #       sys.exit(1)

if __name__ == '__main__' :
    b_log.init()
    run_tests()
    print("OK!")
    input()
        
