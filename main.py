# Define the Node class for building the tree
class Node:
    def __init__(self, key_part, full_key):
        self.key_part = key_part  # The part of the key at this level
        self.full_key = full_key  # The full key up to this node
        self.value = ''           # The value associated with this key
        self.children = {}        # Dictionary of child nodes

def parse_key(key):
    """
    Parse the key into its hierarchical components.
    """
    pattern = re.compile(r'^([A-Z])(\d+)?([a-z])?(i{1,3})?$')
    match = pattern.match(key)
    if not match:
        raise ValueError(f"Invalid key format: {key}")
    groups = match.groups()
    levels = [g for g in groups if g]
    return levels

def build_tree(rule_dict):
    """
    Build a tree representation of the rules.
    """
    root = Node('', '')
    for key, value in rule_dict.items():
        levels = parse_key(key)
        current_node = root
        full_key = ''
        for level in levels:
            full_key += level
            if level not in current_node.children:
                current_node.children[level] = Node(level, full_key)
            current_node = current_node.children[level]
        current_node.value = value
    return root

def traverse_stack(node, accumulated_value, final_dict):
    """
    Traverse the tree, accumulating values and building the final dictionary.
    """
    accumulated_value += node.value
    if node.full_key:
        final_dict[node.full_key] = accumulated_value
    for child in node.children.values():
        traverse_stack(child, accumulated_value, final_dict)

def concat_level4(rule_dict):
    """Concatenate sub-rules by stripping 'i', 'ii', 'iii' suffixes."""
    result = {}
    subrule_pattern = re.compile(r"^([A-Z]\d?[a-z]?)(i{1,3})?$")
    for k, v in rule_dict.items():
        match = subrule_pattern.match(k)
        if match:
            stripped_key = match.group(1)
            if stripped_key not in result:
                result[stripped_key] = ''
            result[stripped_key] += v
    return result

def stack_rules(rule_dict):
    """
    Stack the rules by accumulating values along the tree paths.
    """
    # Build the tree from the rule dictionary
    root = build_tree(rule_dict)
    # Initialize the final dictionary to store the processed rules
    final_dict = {}
    # Traverse the tree and build the final dictionary
    traverse_stack(root, '', final_dict)
    return final_dict

def filter_rules(rule_dict, rule_cat_cols):
    """Filter the dictionary to keep only keys present in rule_cat_cols."""
    rule_cat_set = set(rule_cat_cols)
    filtered_dict = {k: v for k, v in rule_dict.items() if k in rule_cat_set}
    return filtered_dict
