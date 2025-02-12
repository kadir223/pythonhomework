#q1 Get Value
def get_value(d, key, default=None):
    return d.get(key, default)

#q2 Check Key
def check_key(d, key):
    return key in d

#q3 Count Keys
def count_keys(d):
    return len(d)

#q4 Get All Keys
def get_all_keys(d):
    return list(d.keys())

#q5 Get All Values
def get_all_values(d):
    return list(d.values())

#q6 Merge Dictionaries
def merge_dicts(d1, d2):
    return {**d1, **d2}

#q7 Remove Key
def remove_key(d, key):
    d.pop(key, None)
    return d

#q8 Clear Dictionary
def clear_dict():
    return {}

#q9 Check if Dictionary is Empty
def is_dict_empty(d):
    return not bool(d)

#q10 Get Key-Value Pair
def get_key_value(d, key):
    return (key, d[key]) if key in d else None

#q11 Update Value
def update_value(d, key, value):
    d[key] = value
    return d

#q12 Count Value Occurrences
def count_value_occurrences(d, value):
    return list(d.values()).count(value)

#q13 Invert Dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}

#q14 Find Keys with Value
def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

#q15 Create a Dictionary from Lists
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

#q16 Check for Nested Dictionaries
def check_nested_dict(d):
    return any(isinstance(v, dict) for v in d.values())

#q17 Get Nested Value
def get_nested_value(d, key1, key2):
    return d.get(key1, {}).get(key2)

#q18 Create Default Dictionary
def create_default_dict(default_value):
    from collections import defaultdict
    return defaultdict(lambda: default_value)

#q19 Count Unique Values
def count_unique_values(d):
    return len(set(d.values()))

#q20 Sort Dictionary by Key
def sort_dict_by_key(d):
    return dict(sorted(d.items()))

#q21 Sort Dictionary by Value
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

#q22 Filter by Value
def filter_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

#q23 Check for Common Keys
def check_common_keys(d1, d2):
    return set(d1.keys()) & set(d2.keys())

#q24 Create Dictionary from Tuple
def create_dict_from_tuple(t):
    return dict(t)

#q25 Get the First Key-Value Pair
def get_first_key_value(d):
    return next(iter(d.items()), None)
