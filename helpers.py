import re

init_headers = substrings = ['0 entity_prototypes: ', '0 item_prototypes: ', '0 recipes: ']

def process_initial_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    return split_on_multiple_substrings_to_dict(text,init_headers)
    
def split_on_multiple_substrings_to_dict(text, substrings):
    # Create a pattern by joining the substrings with a "|" (OR) operator
    pattern = '|'.join(re.escape(sub) for sub in substrings)
    # Use re.split() to split the text based on the pattern
    parts = re.split(pattern, text)
    # Use re.findall() to find all occurrences of the substrings
    keys = re.findall(pattern, text)
    print(keys)
    # Create a dictionary with the substrings as keys and the text following them as values
    result_dict = {}
    for key, value in zip(keys, parts):
        # print(key)
        items = value.split('$')
        items_dict = {}
        for x in items:
            temp = x.split(' ')
            items_dict[temp[0]] = temp[1:] 

        result_dict[key[2:-2]] = items_dict
    
    return result_dict

