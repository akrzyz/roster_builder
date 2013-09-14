#b_xmlreader

import xml.etree.ElementTree as ET
from b_classes import *
import logging as LOG

def read_item(node):
    name = node.find("name")
    if name is not None : name = name.text
    value = node.find("value")
    if value is not None : value = value.text
    if (name is not None) and (value is not None):
        return b_item(name,value)
    else :
        LOG.warn("unable to read item")
        return None

def read_resource(node):
    name = node.find("name")
    if name is not None : name = name.text
    desc = node.find("desc")
    if desc is not None : desc = desc.text
    spec = node.find("spec")
    if spec is not None : spec = spec.text
    if desc is None : desc = ""
    if spec is None : spec = ""
    if (name is not None) and (desc is not None) and (spec is not None):
        return b_resource(name,desc,spec)
    else :
        LOG.warn("unable to read resource")
        return None

def read_property(node):
    name = node.find("name")
    if name is not None : name = name.text
    value = node.find("value")
    if value is not None :
        value = value.text
        if value is None : value = ""
    options = node.attrib.get('options')
    if (name is not None) and (value is not None) and (options is not None):
        return b_property(name,value,int(options))
    else :
        LOG.warn("unable to read property")
        return None

def read_stats(node):
    stats_str = node.text
    stats = b_stats()
    if stats_str is None : return stats
    stats_str = stats_str.split(',')
    for line in stats_str:
        line = line.split('=')
        if len(line) == 2:
            stats[line[0]] = line[1]
        else :
            LOG.warn("stats incorect format: " + str(stats_str))
    return stats


def read_list(node):
    opt = node.attrib.get('options')
    name = node.attrib.get('name')
    if (opt is not None) and (name is not None) :
        list = b_list(name, int(opt))
        for element in node :
            list.append(f_read(element))
        return list
    else:
        LOG.warn("unable to read list")
        return None

def read_map(node):
    name = node.attrib.get('name')
    if name is None :
        LOG.warn("unable to read map, no name given")
        return None
    map = b_map(name)
    for element in node :
        element_name = element.get('name')
        if element_name is not None :
            map[element_name].extend(f_read(element))
        else:
            LOG.warn("unable to read list in map: "+ str(name) +", no name given")
            pass
    return map

def read_unit(node):
    unit = b_unit()
    for subNode in node:
        if subNode.tag == "stats":
            unit.stats = f_read(subNode)
        elif subNode.tag == "count":
            unit.count = f_read(subNode)
        elif subNode.tag == "list" and subNode.get("name") != None and subNode.get("name") == "properties":
            unit.properties = f_read(subNode)
        elif subNode.tag == "map" and subNode.get("name") != None and subNode.get("name") == "resources":
            unit.resources = f_read(subNode)
        else:
            LOG.warn("unknown element in unit: " + str(subNode.tag))
    return unit

def read_roster(node):
    roster = b_roster()
    for subNode in node:
        if subNode.tag == "list" and subNode.get("name") != None and subNode.get("name") == "properties":
            roster.properties = f_read(subNode)
        elif subNode.tag == "list" and subNode.get("name") != None and subNode.get("name") == "units":
            roster.units = f_read(subNode)
        elif subNode.tag == "map" and subNode.get("name") != None and subNode.get("name") == "resources":
            roster.resources = f_read(subNode)
        else:
            LOG.warn("unknown element in roster: " + str(subNode.tag))
    return roster
    
def read_count(node):
    l_min = node.find('min')
    l_max = node.find('max')
    l_val = node.find('count')
    l_step = node.find('step')
    if l_min != None and l_max != None and l_val != None and l_step != None :
        return b_count(l_val.text, l_min.text, l_max.text, l_step.text)
    else:
        LOG.warn('unable to read count')
        return None
#################################################
f_read_table = {
    'item'      : read_item,
    'resource'  : read_resource,
    'stats'     : read_stats,
    'property'  : read_property,
    'list'      : read_list,
    'map'       : read_map,
    'unit'      : read_unit,
    'roster'    : read_roster,
    'count'     : read_count
         }

def f_read(node):
    try:
        return f_read_table[node.tag](node)
    except:
        LOG.warn("unable to read node: " + str(node.tag))
        return None

def f_read_file(file):
    LOG.info("reading file: " + str(file))
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        object = f_read(root)
        return object
    except:
        LOG.warn("exception during reading file: " + str(file))
        return None
    

