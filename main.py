import re
from collections import defaultdict

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

def traverse(node, accumulated_value, rule_cat_cols, final_dict):
    """
    Traverse the tree, accumulating values and building the final dictionary.
    """
    if node.full_key in rule_cat_cols:
        node.value = accumulated_value + node.value
        final_dict[node.full_key] = node.value
    else:
        accumulated_value += node.value
    for child in node.children.values():
        traverse(child, accumulated_value, rule_cat_cols, final_dict)

def process_rules(rule_dict, rule_cat_cols):
    """
    Process the rules according to the specified requirements.
    """
    # Build the tree from the rule dictionary
    root = build_tree(rule_dict)
    # Initialize the final dictionary to store the processed rules
    final_dict = {}
    # Traverse the tree and build the final dictionary
    traverse(root, '', set(rule_cat_cols), final_dict)
    return final_dict

# Example usage:
if __name__ == "__main__":
    # Given rule dictionary
    rule_dict = {
        'A': 'some test A ',
        'B': 'Some test B ',
        'B1': 'some text B1 ',
        'B1a': 'some text B1a ',
        'B1ai': 'some text B1ai ',
        'B1aii': 'some test B1aii ',
    }

    # Given rule categories to keep
    rule_cat_cols = [
        "A", "B", "C1a", "C1b", "C1c", "C1d", "C1e", "C1f", "C1g", "C2a", "C2b", "C2c",
        "C2d", "C2e", "C2f", "C2g", "C2h", "C2i", "C3a", "C3b", "C3c", "C3d", "C3e", "C3f",
        "C3g", "C3h", "C3i", "D1", "D2", "D3", "D4", "E", "F", "G1", "G2", "G3", "G4", "G5",
        "H1", "H2", "H3", "H4", "H5", "K1", "K2", "K3", "K4", "K5", "K6", "L1", "L2", "L3",
        "M1", "M2", "M3", "M4", "NA"
    ]

    # Process the rules
    final_dict = process_rules(rule_dict, rule_cat_cols)

    # Print the final dictionary
    for key, value in final_dict.items():
        print(f"{key}: {value}")
