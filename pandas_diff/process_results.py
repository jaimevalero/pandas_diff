

def get_gey_values(row, keys):
    key_values=""
    for key in keys:
        key_values += str(row[key]) + ","
    key_values = key_values.rstrip(',')
    return key_values

def format_results_create_delete(row  ,operation, keys) -> dict:
    """ Process create and delete entry"""
    key_values = get_gey_values(row, keys)
    d = {
        "operation"         : operation,
        "object_keys"       : keys,
        "object_values"     : key_values,
        "object_json"       : row.to_dict(),
    }
    return d

def format_results_modify( row, keys , attribute_changed ,  old_value,  new_value ) -> dict:
    """ Process modification entry"""
    key_values = get_gey_values(row, keys)

    d = {
        "operation"         : "modify",
        "object_keys"       : keys,
        "object_values"     : key_values,
        "object_json"       : row.to_dict(),
        "attribute_changed" : attribute_changed,
        "old_value"         : old_value,
        "new_value"         : new_value
    }
    return d
