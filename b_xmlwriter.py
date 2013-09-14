#b_xmlwriter

import xml.etree.ElementTree as ET
from xml.dom import minidom
from b_classes import *
import re
import logging as LOG
##################################################
# helper functions
##################################################
""" addOptions(element, node) : append attribute options if element is instance of b_options """
def addOptions(element, node):
    if isinstance(element, b_options) :
        node.attrib['options'] = str(element.getOpt())

""" addName(element, node) : append attribute name if element is instance of b_name """
def addName(element, node):
    if isinstance(element, b_name) :
        node.attrib['name'] = element.name

#list with function adding attributes to node
attribFooList = [addOptions, addName];

""" append attributes to node depending of element type """
def appendAttribs(element, node):
    for foo in attribFooList:
        foo(element, node)

##################################################
# write functions
##################################################
"""
write_item(item) return xml node containing item from list
* item is instance of b_item
* if item is instance of b_options, options are add as arrtibute
"""
def write_item(item):
    node = ET.Element(item.type_name)
    appendAttribs(item, node)
    ET.SubElement(node, "name").text = str(item.name)
    ET.SubElement(node, "value").text = str(item.value)
    return node

"""
write_resource(recource) return xml node containing resource from list
* resource is instance of b_resource
* if item is instance of b_options, options are add as arrtibute
"""    
def write_resource(recource):
    node = ET.Element(recource.type_name)
    appendAttribs(recource, node)
    ET.SubElement(node, "name").text = str(recource.name)
    ET.SubElement(node, "desc").text = str(recource.desc)
    ET.SubElement(node, "spec").text = str(recource.spec)
    return node

"""
write_property(property) return xml node containing resource from list
* property is instance of b_property
* if item is instance of b_options, options are add as arrtibute
"""   
def write_property(property):
    node = ET.Element(property.type_name)
    appendAttribs(property, node)
    ET.SubElement(node, "name").text = str(property.name)
    ET.SubElement(node, "value").text = str(property.value)
    return node

"""
write_count(count) return xml node containing resource from list
* count is instance of b_count
* if item is instance of b_options, options are add as arrtibute
"""      
def write_count(count):
    node = ET.Element(count.type_name)
    appendAttribs(count, node)
    ET.SubElement(node, "count").text = str(count.count)
    ET.SubElement(node, "min").text = str(count.min)
    ET.SubElement(node, "max").text = str(count.max)
    ET.SubElement(node, "step").text = str(count.step)
    return node
    
"""
write_list(list) return xml node containing list of items.
* list is instance od list
* items in list are instance od dict
* if list is instance of b_options, options are add as arrtibute
"""
def write_list(list):
    node = ET.Element(list.type_name)
    appendAttribs(list, node)
    for element in list :
        node.append(f_write(element))
    return node

"""
write_map(list) return xml node containing map of lists
* list is instance od list
* items in list are instance od dict
* map is iterable
* if map is instance of b_options, options are add as arrtibute
"""
def write_map(map):
    node = ET.Element(map.type_name)
    appendAttribs(map, node)
    for list in map.values():
        node.append(f_write(list))
    return node

def write_stats(stats):
    node = ET.Element(stats.type_name)
    appendAttribs(stats, node)
    stat_str = '';
    for key, val in stats.items():
        stat_str += key + "=" + val +","
    if len(stat_str) > 0 : stat_str = stat_str[:-1]
    node.text = stat_str
    return node

def write_unit(unit):
    node = ET.Element(unit.type_name)
    appendAttribs(unit, node)      
    node.append(f_write(unit.properties))
    node.append(f_write(unit.stats))
    node.append(f_write(unit.count))    
    node.append(f_write(unit.resources))
    return node

def write_roster(roster):
    node = ET.Element(roster.type_name)
    appendAttribs(roster, node)
    node.append(f_write(roster.properties))
    node.append(f_write(roster.units))
    node.append(f_write(roster.resources))
    return node
#################################################
f_write_table = {
    'item'       : write_item,
    'property'   : write_property,
    'resource'   : write_resource,
    'count'      : write_count,
    'stats'      : write_stats,
    'list'       : write_list,
    'map'        : write_map,
    'unit'       : write_unit,
    'roster'     : write_roster
          }

def f_write(element):
    try:
        return f_write_table[element.type_name](element)
    except:
        LOG.warn("exception during f_write typeof: " + str(type(element)))
        return None

def f_write_file(file_name, obj):
    try:
        LOG.info("writing file: "+ str(file_name))
        file = open(file_name,'w')
        node = f_write(obj)
        xmlStr = ET.tostring(node)
        #make it pretty!
        reparsed = minidom.parseString(xmlStr)
        xmlStr = reparsed.toprettyxml()
        text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
        xmlStr = text_re.sub('>\g<1></', xmlStr)
        #end of making pretty
        file.write(xmlStr)
        file.close()
    except:
        LOG.warn("exceptiong during writing file: " + str(file_name))
        return False
    return True
