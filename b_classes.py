from b_utils import *
################################################################################
#   Helper const
################################################################################
VISABLE = 0x1;
EDITABLE = 0x2;
COUNTABLE = 0x4;

################################################################################
#   Helper Classes
################################################################################
class b_options:
    #options
    __options = None
    def __init__(self,opt=VISABLE | EDITABLE | COUNTABLE):
        self.__options = opt;
    def getOpt(self,opt=0xFF):
        return self.__options & opt;
    def setOpt(self,opt):
        self.__options = self.__options | opt;
    def clearOpt(self,opt):
        self.__options = self.__options & (~opt);
    def __repr__(self):
        return "__options [options: " + str(self.__options) + " ]"

class b_name:
    __name = None
    @property
    def name(self):
        return self.__name
    def __init__(self, name):
        self.__name = name
    def __repr__(self):
        return "b_name [name: "+ str(self.name) +" ]"

class b_type_name:
    __type_name = None
    @property
    def type_name(self):
        return self.__type_name
    def __init__(self, type_name):
        self.__type_name = type_name
    def __repr__(self):
        return "b_type_name [type_name: "+ str(self.type_name) +" ]"

################################################################################
#   Real Classes
################################################################################
class b_item(b_type_name):
    name = None
    value = None
    def __init__(self, name, value):
        b_type_name.__init__(self,'item')
        self.name = name;
        self.value = value;
    def __eq__(self, ref):
        return isinstance(ref,b_item) and self.name == ref.name and self.value == ref.value and self.type_name == ref.type_name;
    def __repr__(self):
        return "b_item [name: "+ str(self.name) +", value: "+ str(self.value) +" ]"

class b_resource(b_type_name):
    name = None;
    desc = None;
    spec = None;
    def __init__(self, name, description="", spec=""):
        b_type_name.__init__(self, 'resource')
        self.name = name
        self.desc = description
        self.spec = spec
    def __eq__(self, ref):
        return isinstance(ref,b_resource) and self.name == ref.name and self.desc == ref.desc and self.spec == ref.spec and self.type_name == ref.type_name;
    def __repr__(self):
        return "b_resource [name: "+ str(self.name) +", desc: "+ str(self.desc) +", spec: "+ str(self.spec) +" ]"

class b_property(b_options, b_type_name):
    name = None;
    value = None;
    def __init__ (self,name,value="",options=VISABLE | EDITABLE | COUNTABLE):
        b_options.__init__(self, options)
        b_type_name.__init__(self,'property')
        self.name = name;
        self.value = value;
    def __eq__(self, ref):
        return isinstance(ref,b_property) and self.name == ref.name and self.value == ref.value and self.type_name == ref.type_name;
    def __repr__(self):
        return "b_property [opt : " + str(self.getOpt()) + ", name: "+ str(self.name) +", value: "+ str(self.value) +" ]"

class b_stats(dict, b_type_name):
    def __init__(self):
        b_type_name.__init__(self,'stats')
        basic_stats = {}

class b_count(b_type_name):
    count = None;
    min = None;
    max = None;
    step = None;
    def __init__(self,p_count = 1, p_min = 1, p_max = 1, p_step = 1):
        b_type_name.__init__(self,'count')
        self.count = int(p_count);
        self.min = int(p_min);
        self.max = int(p_max);
        self.step = int(p_step);

    def increment(self):
        if self.count + self.step <= self.max :
            self.count = self.step + self.count
            return True
        else:
            return False
    def decrement(self):
        if self.count - self.step >= self.min :
            self.count = self.count - self.step;
            return True
        else:
            return False
    def __eq__(self, ref):
        return isinstance(ref,b_count) and self.count == ref.count and self.min == ref.min and self.max == ref.max and self.step == ref.step and self.type_name == ref.type_name;
    def __repr__(self):
        return "b_count [count: "+ str(self.count) +", min: "+ str(self.min) +", max: "+ str(self.max) +", step: "+ str(self.step) +" ]"

class b_list(list, b_options, b_name, b_type_name):
    def __init__(self, name, options=VISABLE | EDITABLE | COUNTABLE):
        b_options.__init__(self, options)
        b_name.__init__(self, name)
        b_type_name.__init__(self, 'list')

    def getByName(self,name):
        for i in self:
            if hasattr(i,'name'):
                i_name = i.name
            elif hasattr(i,'get'):
                i_name = i.get('name')
            else:
                continue
            if i_name == name:
                return i
        return None

    def empty(self):
        if len(self) == 0 :
            return True
        return False

class b_map(dict, b_name, b_type_name):
    #operator obj[key]
    def __getitem__(self,key):
        if self.get(key) is None:
            self[key] = b_list(key);
        return self.get(key);
    def __init__(self, name):
        b_name.__init__(self, name)
        b_type_name.__init__(self,'map')

class b_unit(b_type_name):
    properties = None;
    stats = None;
    count = None;
    resources = None;
    def __init__(self):
        b_type_name.__init__(self,'unit')
        self.stats = b_stats();
        self.count = b_count();
        self.resources = b_map('resources');
        self.properties = b_list('properties')
        self.properties.extend([b_property("name"), b_property("type"), b_property('basic_cost','0'), b_property('inc_cost','0')]);
    def __eq__(self, ref):
        return isinstance(ref,b_unit) and self.properties == ref.properties and self.stats == ref.stats and self.count == ref.count and self.resources == ref.resources and self.type_name == ref.type_name;
    def __repr__(self):
        return "b_unit[\nproperties: " + str(self.properties) +"\nstats: "+ str(self.stats) +"\ncount: "+ str(self.count) +"\nresources: "+ str(self.resources) +"\n]"

    @property
    def name(self):
        return self.properties.getByName("name")

    def count_value(self):
        l_value = 0
        #basic unit cost
        l_tmp = self.properties.getByName('basic_cost')
        if l_tmp != None : l_value += int(l_tmp.value)
        #cost of additional members
        l_tmp = self.properties.getByName('inc_cost')
        if l_tmp != None : l_value += (self.count.count - self.count.min)*int(l_tmp.value)
        #cost of resources
        for list in self.resources.values() :
            if list.getOpt(COUNTABLE) :
                for item in list :
                    val = item.value
                    if val != None :
                        l_value += int(val)
        set_value(self.properties, l_value)
        return l_value

    def resolve_spec(self):
        pass

class b_roster(b_type_name):
    properties = None;
    units = None;
    resources = None;
    def __init__(self):
        b_type_name.__init__(self,'roster')
        self.units = b_list('units')
        self.resources = b_map('resources')
        self.properties = b_list('properties')
        self.properties.extend([b_property("game_name"), b_property("army_name")])
    def __eq__(self, ref):
        return isinstance(ref,b_roster) and self.properties == ref.properties and self.units == ref.units and self.resources == ref.resources and self.type_name == ref.type_name;
    def __repr__(self):
        return "b_roster[\nproperties: "+ str(self.properties) +"\nunits: "+ str(self.units) +"\nresources: "+ str(self.resources) +"\n]"

    def count_value(self):
        l_value = 0;
        #units cost
        for unit in self.units :
            val = unit.properties.getByName('value')
            if val != None :
                l_value += int(val.value)
            else:
                l_value += u.count_value()
        #resources cost
        for list in self.resources :
            if list.getOpt(COUNTABLE) :
                for item in list :
                    l_value += int(item.value)
        #properties cost
        for prop in self.properties :
            if prop.getOpt(COUNTABLE) :
                l_value += int(prop.value)
        set_value(self.properties, l_value)
        return l_value

#####################################################
# helper functions
#####################################################
#set value property
def set_value(list,val):
    prop_val = list.getByName('value')
    if prop_val == None:
        list.append(b_property('value',str(val),VISABLE))
    else:
        prop_val['value'] = str(val)
        prop_val.clearOpt(EDITABLE | COUNTABLE)
        prop_val.setOpt(VISABLE)
