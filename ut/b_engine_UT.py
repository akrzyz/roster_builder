#b_xmlwriter_UT
import sys
sys.path.append('../')
from b_classes import *
from b_xmlwriter import *
from b_engine import *
import xml.etree.ElementTree as ET
import traceback
import b_log
import logging as LOG

################################################
# Testcases
################################################

def test_init():
    e = b_engine()
    assert e.config_file == 'config.txt'
    assert e.config is not None
    conf_ref = b_list('config')
    conf_ref.append(b_item('w40k','./data/w40k_config.txt'))
    conf_ref.append(b_item('Necromunta','./data/necromunda_config.txt'))
    conf_ref.append(b_item('Bloodbowl','./data/bloodbowl_config.txt'))
    assert e.config == conf_ref
    LOG.info('test_init ok')
    
def test_init_game():
    e = b_engine()
    assert e.config.getByName('w40k') is not None

    game_conf_ref = b_map('game_config')
    game_conf_ref['Space Marines'].append(b_item('unit_factory_map','./data/SM_factory.txt'))
    game_conf_ref['Space Marines'].append(b_item('resources_map','./data/SM_resources_list.txt'))
    game_conf_ref['Space Marines'].append(b_item('price_map','./data/SM_price_list.txt'))
    game_conf_ref['Tau'].append(b_item('unit_factory_map','./data/tau_factory.txt'))
    game_conf_ref['Tau'].append(b_item('price_map','./data/tau_price_list.txt'))
    game_conf_ref['Tau'].append(b_item('resources_map','./data/tau_resources_list.txt'))

    e.init_game('w40k')
    assert e.game_config_file == './data/w40k_config.txt'
    assert e.game_config == game_conf_ref
    
    assert not e.game_config['Tau'].empty()
    assert e.game_config['Orks'].empty()
    LOG.info('test_init_game ok')
    
def test_init_unit_factory():
    e = b_engine()    
    e.init_game('w40k')
    e.army_config = e.game_config['Space Marines']

    factory_ref = b_map('unit_factory')
    factory_ref['troops'].append(b_item('Tactical squad','./data/unit_prototypes/tactical_squad.txt'))
    factory_ref['troops'].append(b_item('Scout squad','./data/unit_prototypes/scout_squad.txt'))
    factory_ref['elite'].append(b_item('Terminator squad','./data/unit_prototypes/terminator_squad.txt'))
    factory_ref['elite'].append(b_item('Drednought','./data/unit_prototypes/drednought.txt'))
    e._b_engine__init_unit_factory_map()
    assert e.unit_factory_map == factory_ref
    LOG.info('test_init_unit_factory ok')

def test_init_resource_map():
    e = b_engine()    
    e.init_game('w40k')
    e.army_config = e.game_config['Space Marines']

    map_ref = b_map('resources_map')
    map_ref['basic weapons'].append(b_resource('lasgun','latarka'))
    map_ref['basic weapons'].append(b_resource('boltgun','ra ta ta'))
    map_ref['basic weapons'].append(b_resource('h.bolter','tra ta ta!'))
    map_ref['closecombat weapons'].append(b_resource('power weapon','ciach'))
    map_ref['closecombat weapons'].append(b_resource('power fist','bam','S * 2'))
    map_ref['closecombat weapons'].append(b_resource('knife','ciach ciach'))
    map_ref['skills'].append(b_resource('jump','hop hop'))
    map_ref['skills'].append(b_resource('run','run forest run','M + 2'))
    map_ref['skills'].append(b_resource('hide','you cant see me'))
    
    e._b_engine__init_resources_map()
    assert e.resources_map == map_ref
    LOG.info('test_init_resource_map ok')
    
    
def test_init_price_map():
    e = b_engine()    
    e.init_game('w40k')
    e.army_config = e.game_config['Space Marines']  

    map_ref = b_map('price_map')    
    map_ref['Tactical squad'].append(b_item('basic weapons','data/price_lists/basic_weapons.txt'))
    map_ref['Tactical squad'].append(b_item('closecombat weapons','data/price_lists/closecombat_weapons.txt'))
    map_ref['Scout squad'].append(b_item('basic weapons','data/price_lists/basic_weapons.txt'))
    map_ref['Scout squad'].append(b_item('skills','data/price_lists/skills.txt'))
    map_ref['Terminator squad'].append(b_item('basic weapons','data/price_lists/basic_weapons.txt'))
    map_ref['Terminator squad'].append(b_item('closecombat weapons','data/price_lists/closecombat_weapons.txt'))
    map_ref['Terminator squad'].append(b_item('skills','data/price_lists/skills.txt'))
    
    e._b_engine__init_price_map()
    assert e.price_map == map_ref
    LOG.info('test_init_price_map ok')
 

def test_init_army(): 
    e = b_engine()    
    e.init_game('w40k')
    e.init_army('Space Marines')
    
    factory_ref = b_map('unit_factory')
    factory_ref['troops'].append(b_item('Tactical squad','./data/unit_prototypes/tactical_squad.txt'))
    factory_ref['troops'].append(b_item('Scout squad','./data/unit_prototypes/scout_squad.txt'))
    factory_ref['elite'].append(b_item('Terminator squad','./data/unit_prototypes/terminator_squad.txt'))
    factory_ref['elite'].append(b_item('Drednought','./data/unit_prototypes/drednought.txt'))
    assert e.unit_factory_map == factory_ref
    
    map_ref = b_map('resources_map')
    map_ref['basic weapons'].append(b_resource('lasgun','latarka'))
    map_ref['basic weapons'].append(b_resource('boltgun','ra ta ta'))
    map_ref['basic weapons'].append(b_resource('h.bolter','tra ta ta!'))
    map_ref['closecombat weapons'].append(b_resource('power weapon','ciach'))
    map_ref['closecombat weapons'].append(b_resource('power fist','bam','S * 2'))
    map_ref['closecombat weapons'].append(b_resource('knife','ciach ciach'))
    map_ref['skills'].append(b_resource('jump','hop hop'))
    map_ref['skills'].append(b_resource('run','run forest run','M + 2'))
    map_ref['skills'].append(b_resource('hide','you cant see me'))
    assert e.resources_map == map_ref
    
    map_ref = b_map('price_map')    
    map_ref['Tactical squad'].append(b_item('basic weapons','data/price_lists/basic_weapons.txt'))
    map_ref['Tactical squad'].append(b_item('closecombat weapons','data/price_lists/closecombat_weapons.txt'))
    map_ref['Scout squad'].append(b_item('basic weapons','data/price_lists/basic_weapons.txt'))
    map_ref['Scout squad'].append(b_item('skills','data/price_lists/skills.txt'))
    map_ref['Terminator squad'].append(b_item('basic weapons','data/price_lists/basic_weapons.txt'))
    map_ref['Terminator squad'].append(b_item('closecombat weapons','data/price_lists/closecombat_weapons.txt'))
    map_ref['Terminator squad'].append(b_item('skills','data/price_lists/skills.txt'))    
    assert e.price_map == map_ref
    
    LOG.info('test_init_army ok')
    
    
def test_create_unit(): 
    e = b_engine()    
    e.init_game('w40k')
    e.init_army('Space Marines')
    
    unit_ref = b_unit()
    unit_ref.properties.getByName('name').value = 'TS #1'
    unit_ref.properties.getByName('type').value = 'Tactical squad'
    unit_ref.resources['basic weapons'].append(b_item('bolter','5'))
    unit_ref.resources['basic weapons'].append(b_item('laspistol','0'))
    unit_ref.resources['closecombat weapons'].append(b_item('knife','0'))
    unit_ref.resources['skills'].append(b_item('trugrid','0'))
    unit_ref.stats['WS'] = '4'
    unit_ref.stats['BS'] = '4'
    unit_ref.stats['S'] = '4'
    unit_ref.stats['T'] = '4'
    unit_ref.stats['A'] = '4'
    unit_ref.stats['I'] = '4'
    unit_ref.stats['A'] = '1'
    unit_ref.stats['Sv'] = '3+'    
    
    assert e.create_unit('troops','Tactical squad') == unit_ref    
    assert e.create_unit('feawfe','Tactical squad') == None    
    assert e.create_unit('troops','dsaasdsadsadsa') == None
    LOG.info('test_create_unit ok')
    
def test_get_price_list():
    e = b_engine()    
    e.init_game('w40k')
    e.init_army('Space Marines')
    
    price_map_ref = b_map('price_map')        
    price_map_ref['basic weapons'].append(b_item('bolter','40'))
    price_map_ref['basic weapons'].append(b_item('lasgun','15'))
    price_map_ref['basic weapons'].append(b_item('autogun','10'))
    price_map_ref['closecombat weapons'].append(b_item('knife','5'))
    price_map_ref['closecombat weapons'].append(b_item('sword','10'))
    price_map_ref['closecombat weapons'].append(b_item('powerfist','50'))
    price_map_ref['skills'].append(b_item('run','5'))
    price_map_ref['skills'].append(b_item('jump','0'))
    price_map_ref['skills'].append(b_item('hide','10'))
    
    ts_pm_ref = b_map('Tactical squad')
    ts_pm_ref['basic weapons'] = price_map_ref['basic weapons']
    ts_pm_ref['closecombat weapons'] = price_map_ref['closecombat weapons']

    ss_pm_ref = b_map('Scout squad')
    ss_pm_ref['basic weapons'] = price_map_ref['basic weapons']
    ss_pm_ref['skills'] = price_map_ref['skills']
    
    assert not e.price_map['Tactical squad'].empty()
    assert isinstance(e.price_map['Tactical squad'], b_list)
    assert not e.price_map['Scout squad'].empty()
    assert isinstance(e.price_map['Scout squad'], b_list)
    
    assert e.get_price_list('Tactical squad') == ts_pm_ref
    assert isinstance(e.price_map['Tactical squad'], b_map)
    assert isinstance(e.price_map['Scout squad'], b_list)
    
    assert e.get_price_list('Scout squad') == ss_pm_ref
    assert isinstance(e.price_map['Tactical squad'], b_map)
    assert isinstance(e.price_map['Scout squad'], b_map)
    LOG.info('test_get_price_list ok')

###########################################
#   run testcases
###########################################
def run_tests():
    try:
        LOG.info('#b_xmlwriter_UT start#')
        test_init()
        test_init_game()
        test_init_unit_factory()
        test_init_resource_map()
        test_init_price_map()
        test_init_army()
        test_create_unit()
        test_get_price_list()
        LOG.info('#b_xmlwriter_UT done#')
    except:
        traceback.print_exc()

if __name__ == '__main__' :
    b_log.init_ut()
    run_tests()
    print("OK!")
    input()
