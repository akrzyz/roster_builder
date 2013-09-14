from b_classes import *
import traceback

def __view_item(item, prefix):
    return(prefix + "[" + str(item.name) + " - " + str(item.value) + "]")

def __view_item_short(item, prefix):
    return(prefix + str(item.name))    
    
def __view_property(property, prefix):
    return(prefix + str(property.getOpt()) +" [" + str(property.name) + " - " + str(property.value) + "]") 
    
def __view_resource(resource, prefix):
    return(prefix + "[" + str(resource.name) + " - " + str(resource.desc) + " - " + str(resource.spec) + "]")

def __view_count(count, prefix):
    return(prefix + "[count: "+ str(count.count) + " min: " + str(count.min) + " max: " + str(count.max) + " step: " + str(count.step) + "]")

def __view_stats(stats, prefix):
    ret = prefix + "["
    for key,val in stats.items():
        ret += ("[" + str(key) + " : " + str(val)+"]")
    ret += ("]")
    return ret
    
def __view_list(list,prefix):
    ret=''
    if(prefix):
        ret =+ prefix
    else:
        ret += str(list.name) + ":\n"
    i = 0;
    for elem in list:
        ret += __f_view(elem, str(i)+" - ") + "\n"
        i+=1
    return ret
        
def __view_list_short(list,prefix):
    ret=''
    if(prefix):
        ret =+ prefix
    else:
        ret += str(list.name) + ":\n"
    i = 0;
    for elem in list:
        ret += __f_view_short(elem, str(i)+" - ") + "\n"
        i+=1
    return ret      
        
def __view_map_keys(map,prefix):
    ret = ''
    if(prefix):
        ret += prefix + "{"
    else:
        ret += str(map.name) + ":{\n"        
    i = 0;
    for key in map.keys():
        ret += (str(i) + " - " + str(key) + "\n")
        i+=1 
    ret += "}"
    return ret

def __view_map(map,prefix):
    ret = ''
    if(prefix):
        ret += prefix + "{"
    else:
        ret += str(map.name) + ":{\n"     
    i = 0;
    for key,val in map.items():
        ret += __f_view(val)
        i+=1          
    ret +="}"
    return ret
        
def __view_unit(unit, prefix):
    ret = "unit:{{\n"
    ret += __f_view(unit.properties) + "\n"
    ret += __f_view(unit.stats) + "\n\n"
    ret += __f_view(unit.count) + "\n\n"
    ret += __f_view(unit.resources) + "\n"
    ret += "}}"
    return ret

def __view_unit_short(unit, prefix):
    ret = "unit:{{\n"
    ret += __f_view_short(unit.properties) + "\n"
    ret += __f_view_short(unit.stats) + "\n\n"
    ret += __f_view_short(unit.count) + "\n\n"
    ret += __f_view_short(unit.resources) + "\n"
    ret += "}}"
    return ret
    
def __view_roster(roster, prefix):
    ret = "roster:{{{\n"
    ret += __f_view(roster.properties) + "\n"
    ret += __f_view(roster.units) + "\n"
    ret += __f_view(roster.resources) + "\n"
    ret += "}}}"
    return ret

def __view_roster_short(roster, prefix):
    ret = "roster:{{{\n"
    ret += __f_view_short(roster.properties) + "\n"
    ret += __f_view_short(roster.units) + "\n"
    ret += __f_view_short(roster.resources) + "\n"
    ret += "}}}"
    return ret
    
__f_view_table = {
    'item'       : __view_item,
    'property'   : __view_property,
    'resource'   : __view_resource,
    'count'      : __view_count,
    'stats'      : __view_stats,
    'list'       : __view_list,
    'map'        : __view_map,
    'unit'       : __view_unit,
    'roster'     : __view_roster
}

__f_view_short_table = {
    'item'       : __view_item_short,
    'property'   : __view_property,
    'resource'   : __view_resource,
    'count'      : __view_count,
    'stats'      : __view_stats,
    'list'       : __view_list_short,
    'map'        : __view_map_keys,
    'unit'       : __view_unit_short,
    'roster'     : __view_roster_short
}

def __f_view(element, prefix=""):
    try:
        return __f_view_table[element.type_name](element, prefix)
    except:
        print("exception during f_view typeof: " + str(type(element)))
        traceback.print_exc()
        return None
        
def __f_view_short(element, prefix=""):
    try:
        return __f_view_short_table[element.type_name](element, prefix)
    except:
        print("exception during f_view_short typeof: " + str(type(element)))
        traceback.print_exc()
        return None   

def display(element, prefix=""):
    print(__f_view(element,prefix))
    
def display_short(element, prefix=""):
    print(__f_view_short(element,prefix))    
