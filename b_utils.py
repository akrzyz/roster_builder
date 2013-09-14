#b_utils

def count_value(map):
    value = 0;
    try:
        for item_array in map.values():
            for item in item_array:
                try:
                    value += int(item["value"]);
                except (AttributeError, TypeError, ValueError):
                    pass
    except:
        pass
    return value;
