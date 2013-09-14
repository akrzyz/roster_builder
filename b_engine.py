from b_classes import *
from b_xmlreader import *
from b_xmlwriter import *
import logging as LOG

class b_engine (dict):
    config_file = None
    game_config_file = None
    config = None
    game_config = None
    army_config = None
    roster = None
    resources_map = None
    price_map = None
    unit_factory_map = None

    def __init__(self, p_config_file = 'config.txt'):
        LOG.info("inicializing engine from config: " + str(p_config_file))
        self.config_file = p_config_file
        self.config = f_read_file(p_config_file)

    def init_game(self, p_game):
        LOG.info("inicializing game:" + str(p_game))
        self.game_config_file = self.config.getByName(p_game).value
        self.game_config = f_read_file(self.game_config_file)

    def init_army(self, p_army):
        LOG.info("inicializing army:" + str(p_army))
        self.army_config = self.game_config[p_army]
        self.__init_resources_map()
        self.__init_price_map()
        self.__init_unit_factory_map()

    def start(self):
        self.roster = b_roster()

    def load_roster_and_start(self, p_roster_file):
        self.roster = f_read_file(p_roster_file)


    def __init_resources_map(self):
        LOG.info("inicializing resources_map")
        resources_link_list = f_read_file(self.army_config.getByName('resources_map').value)
        if resources_link_list is not None :
            self.resources_map = b_map(resources_link_list.name)
            for element in resources_link_list :
                resource_name = element.name
                resource_link = element.value
                if (resource_name is not None) and (resource_link is not None) :
                    self.resources_map[element.name].extend(f_read_file(element.value))
                else:
                    LOG.warn('unable to create resource list: name: ' + str(resource_name) + ' from file: ' + str(resource_link))
        if self.resources_map is None :
            LOG.error("inicializing resources_map failed!")
            pass

    def __init_price_map(self):
        LOG.info("inicializing price_map")
        self.price_map = f_read_file(self.army_config.getByName('price_map').value)
        if self.price_map is None :
            LOG.error("inicializing price_map failed!")

    def __init_unit_factory_map(self):
        LOG.info("inicializing unit_factory_map")
        self.unit_factory_map = f_read_file(self.army_config.getByName('unit_factory_map').value)
        if self.unit_factory_map is None :
            LOG.error("inicializing unit_factory_map failed!")

    def create_unit(self, unit_type, unit_name):
        unit = None
        unit_link = self.unit_factory_map[unit_type].getByName(unit_name)
        if unit_link is not None:
            unit = f_read_file(unit_link.value)
        if unit is None :
            LOG.warn('unable to create unit type: ' + str(unit_type) + ', unit name: ' + str(unit_name))
        return unit

    def get_price_list(self, unit_name):
        priceList_ref = self.price_map[unit_name]
        if isinstance(priceList_ref, b_map):
            return priceList_ref
        newPriceMap = b_map(unit_name)
        for i in priceList_ref :
            newPriceMap[i.name].extend( f_read_file(i.value));
        self.price_map[unit_name] = newPriceMap
        return newPriceMap





