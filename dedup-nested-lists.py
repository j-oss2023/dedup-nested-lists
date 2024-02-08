from ansible.errors import AnsibleFilterError
from ansible.utils.display import Display

display = Display()

def deduplicate_nested_lists(value):
    if not isinstance(value, dict):
        raise AnsibleFilterError('Input should be a dict')
    
    new_dict = {}
    for key, list_values in value.items():
        if not isinstance(list_values, list):
            raise AnsibleFilterError('All values should be lists')
        
        # Deduplicate preserving order
        seen = set()
        new_list = []
        for item in list_values:
            if item not in seen:
                seen.add(item)
                new_list.append(item)
        
        new_dict[key] = new_list
    
    return new_dict

class FilterModule(object):
    def filters(self):
        return {
            'dedup_nested_lists': deduplicate_nested_lists
        }
